# schemas.py
from pydantic import BaseModel
from datetime import datetime
import uuid

class ProjectBase(BaseModel):
    title: str
    description: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    name: str
    description: str
    status: str
    uuid: str

    class Config:
        from_attributes = True