from fastapi import FastAPI
from routes.users import user
from routes.destination import destination
from routes.webhook import webhook

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(user)
app.include_router(destination)
app.include_router(webhook)