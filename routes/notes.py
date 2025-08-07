from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from config.db import collection,notes
from models.note import Note
from bson import ObjectId

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )


@router.get('/show-notes')
async def read_notes(request:Request):

    return templates.TemplateResponse(
        request=request, name="notes.html", context={"notes":list(collection.find({}))}
    )


@router.post('/add-note')
async def add_note(request: Request):
    form = await request.form()
    note_dict = dict(form)

    tags_raw = note_dict.get('tags', '')
    tags_list = [tag.strip() for tag in tags_raw.replace(',', ' ').split()]
    note_dict['tags'] = tags_list

    important = form.get('important')
    note_dict['important'] = True if important == "true" or important == "on" else False

    result = collection.insert_one(note_dict)

    inserted_note = collection.find_one({"_id": result.inserted_id})

    return templates.TemplateResponse(
        "success.html",
        {
            "request": request,
            "action": "add",
            "note": inserted_note
        }
    )

@router.get('/edit-note/{note_id}')
def get_edit_note(request:Request,note_id:str):

    note = collection.find_one({"_id": ObjectId(note_id)})

    return templates.TemplateResponse(
        "edit-note.html",
        {
            "request": request,
            "note":note
        }
    )


@router.post('/update-note/{note_id}')
async def update_note(request: Request, note_id: str):
    form = await request.form()
    note_dict = dict(form)

    tags_raw = note_dict.get('tags', '')
    tags_list = [tag.strip() for tag in tags_raw.replace(',', ' ').split()]
    note_dict['tags'] = tags_list

    important = form.get('important')
    note_dict['important'] = True if important == "true" or important == "on" else False

    collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": note_dict}
    )

    updated_note = collection.find_one({"_id": ObjectId(note_id)})

    return templates.TemplateResponse(
        "success.html",
        {
            "request": request,
            "action": "update",  # Different action type
            "note": updated_note
        }
    )


@router.post('/delete-note/{note_id}')
async def delete_note(request: Request, note_id: str):
    collection.delete_one({"_id": ObjectId(note_id)})

    return templates.TemplateResponse(
        "success.html",
        {
            "request": request,
            "action": "delete"
        }
    )
