from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

time_format = "%H:%M"


class Users(SQLModel, table=True):
    user_id: int = Field(default=1, primary_key=True)
    user_name: str = Field(default=None, min_length=3, max_length=50)
    department: str = Field(default=None, min_length=3, max_length=50)
    age: int = Field(default=18, ge=18, le=67)  # legal working-age band

    # relationships
    sessions: List["SessionWork"] = Relationship(back_populates="users")
    projects: List["Projects"] = Relationship(back_populates="users")


class Projects(SQLModel, table=True):
    project_id: int = Field(default=None, primary_key=True)
    project_name: str = Field(default=None, min_length=3, max_length=20)
    description: Optional[str] = Field(default=None, max_length=250)

    # relationships
    user: Users = Relationship(back_populates="projects")


class SessionWork(SQLModel, table=True):
    session_id: int = Field(primary_key=True)
    session_user_id: int = Field(default=None, foreign_key="users.user_id")
    session_project_id: int = Field(default=None, foreign_key="projects.project_id")

    # relationships
    user: Users = Relationship(back_populates="sessions")

    start_time: datetime
    end_time: datetime
    # session_length = start_time - end_time