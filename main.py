import uvicorn
from fastapi import FastAPI, Depends
from database import get_session
from models import Users, Projects, SessionWork
from sqlmodel import select, Session
from request_models import SessionRequest, ProjectRequest, UserRequest


app = FastAPI()


# Users


@app.get('/users', tags=["Users"])
async def get_users(session: Session = Depends(get_session)):
    all_users = session.exec(select(Users)).all()
    return all_users


@app.post('/users/add', tags=["Users"])
async def add_user(req: UserRequest, session: Session = Depends(get_session)):
    user = Users()
    user.user_name = req.user_name
    user.department = req.department
    user.age = req.age
    session.add(user)
    session.commit()
    session.close()
    return "New user added."


@app.put('/users/update/{id}', tags=["Users"])
async def update_user(id: int, new: Users, session: Session = Depends(get_session)):
    selected = session.exec(select(Users).where(Users.user_id == id)).first()

    selected.user_name = new.user_name
    selected.department = new.department
    selected.age = new.age

    session.commit()
    session.refresh(selected)
    return {"message": "User updated successfully", "user": selected}


@app.delete('/users/delete/{id}', tags=["Users"])
async def delete_user(id: int, session: Session = Depends(get_session)):
    selected = session.exec(select(Users).where(Users.user_id == id)).first()
    session.delete(selected)
    session.commit()
    return "User removed successfully."

# Projects


@app.get('/projects', tags=["Projects"])
async def get_projects(session: Session = Depends(get_session)):
    all_projects = session.exec(select(Projects)).all()
    return all_projects


@app.post('/projects/add', tags=["Projects"])
async def add_project(req: ProjectRequest, session: Session = Depends(get_session)):
    project = Projects()
    project.project_name = req.project_name
    project.project_user = req.project_user
    project.description = req.description
    session.add(project)
    session.commit()
    return "Project added successfully."


@app.put('/projects/update/{id}', tags=["Projects"])
async def update_project(id: int, new: Projects, session: Session = Depends(get_session)):
    selected = session.exec(select(Projects).where(Projects.project_id == id)).first()

    selected.project_name = new.project_name
    selected.description = new.description
    selected.project_user = new.project_user

    session.commit()
    session.refresh(selected)
    return "Project updated successfully."


@app.delete('/projects/delete/{id}', tags=["Projects"])
async def delete_project(id: int, session: Session = Depends(get_session)):
    selected = session.exec(select(Projects).where(Projects.project_id == id)).first()
    session.delete(selected)
    session.commit()
    return "Project deleted successfully."


# Work sessions


@app.get('/sessions', tags=["WorkSession"])
async def user_sessions(session: Session = Depends(get_session)):
    all_sessions = session.exec(select(SessionWork)).all()
    return all_sessions


@app.post('/session/add', tags=["WorkSession"])
async def add_session(req: SessionRequest, session: Session = Depends(get_session)):
    work_session = SessionWork()
    work_session.session_user = req.session_user
    work_session.session_project = req.session_project
    work_session.start_time = req.start_time
    work_session.date = req.date
    work_session.end_time = req.end_time
    session.add(work_session)
    session.commit()
    return "Session added successfully."


@app.put('/session/update/{id}', tags=["WorkSession"])
async def update_session(id: int, new: SessionWork, session: Session = Depends(get_session)):
    selected = session.exec(select(SessionWork).where(SessionWork.session_id == id)).first()
    selected.start_time = new.start_time
    selected.end_time = new.end_time
    session.commit()
    session.refresh(selected)


@app.delete('/session/delete/{id}', tags=['WorkSession'])
async def delete_session(id: int, session: Session = Depends(get_session)):
    selected = session.exec(select(SessionWork).where(SessionWork.session_id == id)).first()
    session.delete(selected)
    session.commit()
    return "Session deleted successfully."


if __name__ == "__main__":
    uvicorn.run(app, port=8005, host="localhost")
