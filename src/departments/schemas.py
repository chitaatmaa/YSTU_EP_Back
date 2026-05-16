from typing import Annotated
from pydantic import BaseModel, Field


class DepartmentCreate(BaseModel):
    name: Annotated[str, Field(example='Информационные системы и технологии', max_length=50)]
    short_name: Annotated[str, Field(example='ИСТ', max_length=10)]
    is_actual: Annotated[bool, Field(example=True)] = True


class DepartmentUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Информационные системы и технологии', max_length=50)]
    short_name: Annotated[str | None, Field(example='ИСТ', max_length=10)]
    is_actual: Annotated[bool | None, Field(example=True)] = None


class DepartmentRead(DepartmentCreate):
    id: Annotated[int, Field(example=1)]
