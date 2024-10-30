from pydantic import BaseModel


class CreateUsers(BaseModel):
    username: str
    firstname: str 
    lastname: str
    age: int


class UpdateUsers(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int