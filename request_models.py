from pydantic import BaseModel, Field
from datetime import date, time, timedelta
from typing import Optional


class UsersRequest(BaseModel):
    user_name: str = Field(default=None, min_length=3, max_length=50)
    department: str = Field(default=None, min_length=3, max_length=50)
    age: int = Field(default=18, ge=18, le=67)


class ProjectRequest(BaseModel):
    project_name: str = Field(default=None, min_length=2, max_length=20)
    description: Optional[str] = Field(default=None, max_length=250)
    project_user: str = Field(default=None)


class SessionRequest(BaseModel):
    session_user: str = Field(default=None)
    session_project: str
    date: date
    start_time: time
    end_time: time
