# # main.py
from database.database import Base, engine
from typing import Union
from fastapi import FastAPI

# Ensure the database tables are created
Base.metadata.create_all(bind=engine)
app = FastAPI()

### Move this to controller
@app.get("/create")
def create():
    # Insert a new project
    new_project = Project(name="Test1", description="Brandly description of the new project", status="In Progress")
    return projectCrud.create_project(new_project)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



#####
from database.models.project import Project
import database.models.projectCrud as projectCrud

@app.get("/createDatabase")
def initCreateDatabase():
    # Insert a new project
    new_project = Project(name="Test", description="Brandly description of the new project", status="In Progress")
    projectCrud.create_project(new_project)

