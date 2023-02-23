from fastapi import HTTPException
from db import models
from sqlalchemy.orm.session import Session
from schemas.todo import ToDo
from schemas.util import DeleteStatus


def post_todo(db: Session, title: str, detail: str) -> ToDo:

    todo_orm = models.ToDo(
        title=title,
        detail=detail
    )
    db.add(todo_orm)
    db.commit()
    db.refresh(todo_orm)

    todo = ToDo.from_orm(todo_orm)

    return todo


def put_todo(db: Session, todo_id: str, title: str, detail: str) -> ToDo:
    todo_orm = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if todo_orm == None:
        raise HTTPException(
            status_code=404,
            detail="The todo specified by id is not exist"
        )

    todo_orm.title = todo_orm.title if title is None else title
    todo_orm.detail = todo_orm.detail if detail is None else detail

    db.commit()
    db.refresh(todo_orm)

    todo = ToDo.from_orm(todo_orm)

    return todo


def get_todo_list(db: Session) -> list[ToDo]:
    todo_orm = db.query(models.ToDo).order_by(models.ToDo.created_at).all()

    todo_list = list(map(ToDo.from_orm, todo_orm))
    return todo_list


def get_todo(db: Session, todo_id: str) -> ToDo:
    todo_orm = db.query(models.ToDo).filter(
        models.ToDo.id == todo_id).first()

    if todo_orm is None:
        raise HTTPException(
            status_code=404,
            detail="The todo specified by id is not exist"
        )

    todo = ToDo.from_orm(todo_orm)
    return todo


def delete_todo(db: Session, todo_id: str) -> DeleteStatus:
    result = DeleteStatus(status="OK")

    todo_orm = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()

    if todo_orm != None:
        db.delete(todo_orm)
        db.commit()
    else:
        result.status = "ToDo is not exist"

    return result
