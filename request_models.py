from pydantic import BaseModel, Field, field_validator, FieldValidationInfo
from datetime import date, time
from typing import Optional


class UserRequest(BaseModel):
    user_name: str = Field(default=None, min_length=3, max_length=50)
    department: str = Field(default=None, min_length=3, max_length=50)
    age: int = Field(default=18, ge=18, le=67)


class ProjectRequest(BaseModel):
    project_name: str = Field(default=None, min_length=2, max_length=20)
    description: Optional[str] = Field(default=None, max_length=250)
    # project_user: str = Field(default=None)


class SessionRequest(BaseModel):
    session_user: str
    session_project: str
    date: date
    start_time: time
    end_time: time

    @field_validator('end_time')
    def check_time_difference(cls, end_time, info: FieldValidationInfo):
        start_time = info.data.get('start_time')
        if start_time and end_time <= start_time:
            raise ValueError('End time must be after start time please.')
        return end_time


class ProjectSessionRetriever(BaseModel):
    project_name: str


class UserSessionRetriever(BaseModel):
    user_name: str


class OneProjectOneUser(BaseModel):
    user_name: str
    project_name: str
