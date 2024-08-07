from sqlmodel import SQLModel, Field, select
from typing import Optional
from datetime import datetime


time_format = "%H:%M"


class Users(SQLModel, table=True):
    user_id: int = Field(default=1, primary_key=True)
    user_name: str = Field(default=None, min_length=3, max_length=50)
    department: str = Field(default=None, min_length=3, max_length=50)
    age: int = Field(default=18, ge=18, le=67)  # legal working-age band


class Projects(SQLModel, table=True):
    project_id: int = Field(default=None, primary_key=True)
    project_name: str = Field(default=None, min_length=3, max_length=20)
    description: Optional[str] = Field(default=None, max_length=250)


class SessionWork(SQLModel, table=True):
    session_id: int = Field(primary_key=True)
    start_time: datetime
    end_time: datetime
    project_association: int
