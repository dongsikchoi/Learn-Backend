from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get('/')
async def hello_world():
    return {"Hello" : "World"}

