from fastapi import FastAPI, Depends
from database import get_session
from models import Users, Projects, SessionWork, init
from sqlmodel import select, Session


app = FastAPI()


# Users


@app.get('/users', tags=["Users"])
async def get_users(session: Session = Depends(get_session)):
    all_users = session.exec(select(Users)).all()
    return all_users


@app.post('/users/add', tags=["Users"])
async def add_user(user: Users, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
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


@app.delete('users/delete/{id}', tags=["Users"])
async def delete_user(id: int, session: Session = Depends(get_session)):
    selected = session.exec(select(Users).where(Users.user_id == id)).first()
    session.delete(selected)


# Projects


@app.get('/projects', tags=["Projects"])
async def get_projects(session: Session = Depends(get_session)):
    all_projects = session.exec(select(Projects)).all()
    return all_projects


@app.post('/projects/add', tags=["Projects"])
async def add_project(project: Projects, session: Session = Depends(get_session)):
    session.add(project)
    session.commit()


@app.put('/projects/update/{id}', tags=["Projects"])
async def update_project(id: int, new: Projects, session: Session = Depends(get_session)):
    selected = session.exec(select(Projects).where(Projects.project_id == id))

    selected.project_id = new.project_id
    selected.project_name = new.project_name
    selected.description = new.description

    session.commit()
    session.refresh(selected)


@app.delete('/projects/delete/{id}', tags=["Projects"])
async def delete_project(id: int, session: Session = Depends(get_session)):
    selected = session.exec(select(Projects).where(Projects.project_id == id)).first()
    session.delete(selected)
    session.commit()


# Work sessions


@app.get('/work-sessions', tags=["WorkSession"])
async def user_sessions(session: Session = Depends(get_session)):
    all_sessions = session.exec(select(SessionWork)).all()
    return all_sessions


@app.post('/work-sessions/add', tags=["WorkSession"])
async def add_session(work_session: SessionWork, session: Session = Depends(get_session)):
    session.add(work_session)
    session.commit()
    return "Session added successfully."


@app.put('/work-sessions/update/{id}', tags=["WorkSession"])
async def update_session(id: int, new: SessionWork, session: Session = Depends(get_session)):
    selected = session.exec(select(SessionWork).where(SessionWork.session_id == id)).first()
    selected.start_time = new.start_time
    selected.end_time = new.end_time
    session.commit()
    session.refresh(selected)


@app.delete('/work-session/delete/{id}', tags=['WorkSession'])
async def delete_session(id: int, session: Session = Depends(get_session)):
    selected = session.exec(select(SessionWork).where(SessionWork.session_id == id)).first()
    session.delete(selected)
    session.commit()

