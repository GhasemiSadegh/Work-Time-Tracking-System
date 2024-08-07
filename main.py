from fastapi import FastAPI
from database import init
from models import Users, Projects, SessionWork


app = FastAPI()
init()

# Users


@app.get('/users')
def get_users():
    pass


@app.post('users/add')
def add_user():
    pass


@app.put('users/update')
def update_user():
    pass


@app.delete('users/delete')
def delete_user():
    pass


# Projects


@app.get('/projects')
def get_projects():
    pass


@app.post('projects/add')
def add_project():
    pass


@app.put('projects/update')
def update_project():
    pass


@app.delete('projects/delete')
def delete_project():
    pass
