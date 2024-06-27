# crud.py
from sqlalchemy.orm import Session
from database.models.project import Project
from database.database import engine
db = Session(bind=engine)

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: Project):
    db.add(project)
    print(project)
    db.commit()
    db.refresh(project)
    return project

def update_project(db: Session, project_id: int, name: str = None, description: str = None, status: str = None):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        if name:
            project.name = name
        if description:
            project.description = description
        if status:
            project.status = status
        db.commit()
        db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
    return project
