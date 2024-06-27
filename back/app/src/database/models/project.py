# models.py
from sqlalchemy import Column, Integer, String, Text
from database.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    status = Column(String)
    uuid = Column(String, unique=True)