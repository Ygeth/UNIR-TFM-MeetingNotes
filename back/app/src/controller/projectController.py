# controller/projectController.py
from fastapi import APIRouter, File, UploadFile, Query
from database.models.project import Project
from database.models.projectSchemas import Project, ProjectCreate
from database.models.projectCrud import get_project, create_project
import shutil

router = APIRouter()

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @router.get("/createDummy", response_model=Project)
# async def create_dummy(filename: str = Query(..., filename="The title of the project")):
#     print("filename")
#     print(filename)
    
#     # Create a new project
#     new_project = Project(filename=filename)
#     return create_project(project=new_project, filename=filename)


# @router.post("/projects/", response_model=Project)
# async def upload_project(title: str, description: str, file: UploadFile = File(...)):
#     filename = f"uploads/{file.filename}"
    
#     ## Save the file
#     with open(filename, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     ## Create new project
#     project_create = ProjectCreate(title=title, description=description)
#     return create_project(project=project_create, filename=file.filename)

# @router.get("/projects/{project_id}", response_model=Project)
# def read_project(project_id: int, db: Session = Depends(get_db)):
#     db_project = get_project(db, project_id=project_id)
#     if db_project is None:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return db_project
