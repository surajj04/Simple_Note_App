from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from routes import notes

app = FastAPI()
app.include_router(notes.router)

app.mount("/static", StaticFiles(directory="static"), name="static")



