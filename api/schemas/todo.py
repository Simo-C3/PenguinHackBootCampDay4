from pydantic import BaseModel
from datetime import datetime


class PostToDo(BaseModel):
    title: str
    detail: str

    class Config:
        orm_mode = True


class ToDo(PostToDo):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
