from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, time
from database import init


time_format = "%H:%M"


class Users(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str = Field(default=None, min_length=3, max_length=50)
    department: str = Field(default=None, min_length=3, max_length=50)
    age: int = Field(default=18, ge=18, le=67)  # legal working-age band

    # relationships
    sessions: List["SessionWork"] = Relationship(back_populates="user")
    projects: List["Projects"] = Relationship(back_populates="users")


class Projects(SQLModel, table=True):
    project_id: Optional[int] = Field(default=None, primary_key=True)
    project_name: str = Field(default=None, min_length=2, max_length=20)
    description: Optional[str] = Field(default=None, max_length=250)
    project_user: str = Field(default=None, foreign_key="users.user_name")

    # relationships
    users: List["Users"] = Relationship(back_populates="projects")
    sessions: List["SessionWork"] = Relationship(back_populates="project")


class SessionWork(SQLModel, table=True):
    session_id: Optional[int] = Field(default=None, primary_key=True)
    session_user: str = Field(default=None, foreign_key="users.user_name")
    session_project: str = Field(default=None, foreign_key="projects.project_name")
    date: date
    start_time: time
    end_time: time


    # @property
    # def length(self) -> timedelta:
    #     return self.end_time - self.start_time

    # relationships
    user: "Users" = Relationship(back_populates="sessions")
    project: "Projects" = Relationship(back_populates="sessions")


init()
