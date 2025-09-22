from pydantic import BaseModel
from typing import List, Optional

class TaskBase(BaseModel):
    id: int
    name: str

class TaskCreate(TaskBase):
    name: str

class TaskUpdate(BaseModel):
    name: Optional[str] = None

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
