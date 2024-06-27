# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
# from database.models.project import Project
# import database.models.projectSchemas as projectSchemas
# import database.models.projectCrud as projectCrud



DATABASE_URL = "sqlite:///./projects.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = Session()

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

  # projects = crud.get_projects(db)
  # for project in projects:
  #     print(f"Project ID: {project.id}, Name: {project.name}, Status: {project.status}")

  # # Update a project
  # updated_project = crud.update_project(db, project_id=1, status="Completed")

  # # Delete a project
  # deleted_project = crud.delete_project(db, project_id=1)