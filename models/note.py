from pydantic import BaseModel
from typing import List, Optional


class Note(BaseModel):
    title:str
    content:str
    category:str
    tags:List[str]
    important:Optional[bool] = None
