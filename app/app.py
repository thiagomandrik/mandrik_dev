from fastapi import FastAPI

from app.interfaces.routers import users

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


app.include_router(users.router)
