from typing import Any
from sqlalchemy import Column as Col, String, ForeignKey, DateTime, Text
from uuid import uuid4
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship
import enum
import datetime
from sqlalchemy.sql.functions import func


class Column(Col):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('nullable', False)
        super().__init__(*args, **kwargs)


def generate_uuid():
    return str(uuid4())


@as_declarative()
class Base:
    id: Any
    __name__: Any

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class ToDo(Base):

    __tablename__ = "todo"

    id = Column(String(length=255), primary_key=True, default=generate_uuid)
    title = Column(String(length=50))
    detail = Column(String(length=200))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
