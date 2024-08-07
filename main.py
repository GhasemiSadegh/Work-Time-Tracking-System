from fastapi import FastAPI, Depends
from database import init, get_session, Session
from models import Users, Projects, SessionWork, select


app = FastAPI()


# Users


@app.get('/users', tags=["Users"])
async def get_users(session: Session = Depends(get_session)):
        all_users = session.exec(select(Users)).all()
        session.close()
        return all_users


@app.post('/users/add', tags=["Users"])
async def add_user(user: Users, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.close()
    return "New user added."


@app.put('users/update', tags=["Users"])
async def update_user():
    pass


@app.delete('users/delete', tags=["Users"])
async def delete_user():
    pass


# Projects


@app.get('/projects', tags=["Projects"])
async def get_projects():
    pass


@app.post('projects/add', tags=["Projects"])
async def add_project():
    pass


@app.put('projects/update', tags=["Projects"])
async def update_project():
    pass


@app.delete('projects/delete', tags=["Projects"])
async def delete_project():
    pass


init()
