from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class BookSchemaCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class BookSchemaDelete(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)

class RequestBookCreate(BaseModel):
    parameter: BookSchemaCreate = Field(...)

class RequestBookUpdate(BaseModel):
    parameter: BookSchema = Field(...)

class RequestBookDelete(BaseModel):
    parameter: BookSchemaDelete = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
