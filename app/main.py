from fastapi import FastAPI
from app.router import users, tasks

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(users.router)
app.include_router(tasks.router)
