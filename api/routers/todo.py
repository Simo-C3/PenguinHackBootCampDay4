from fastapi import APIRouter
from fastapi.params import Depends
from schemas.todo import PostToDo, ToDo
from schemas.util import DeleteStatus
from db import get_db
from sqlalchemy.orm.session import Session

from cruds.todo import get_todo_list, get_todo, post_todo, put_todo, delete_todo

import os

todo_router = APIRouter()


@todo_router.get('/', response_model=list[ToDo])
async def get_todo_list_handler(db: Session = Depends(get_db)):
    result = get_todo_list(db)
    return result


@todo_router.get('/{todo_id}', response_model=ToDo)
async def get_todo_handler(todo_id: str = '', db: Session = Depends(get_db)):
    result = get_todo(db, todo_id)
    return result


@todo_router.post('/', response_model=ToDo)
async def post_todo_handler(payload: PostToDo, db: Session = Depends(get_db)):
    result = post_todo(db, payload.title, payload.detail)
    return result


@todo_router.put('/{todo_id}', response_model=ToDo)
async def put_todo_handler(payload: PostToDo, todo_id: str = '', db: Session = Depends(get_db)):
    result = put_todo(db, todo_id, payload.title, payload.detail)
    return result


@todo_router.delete('/{todo_id}', response_model=DeleteStatus)
async def delete_todo_handler(todo_id: str = '', db: Session = Depends(get_db)):
    result = delete_todo(db, todo_id)
    return result
