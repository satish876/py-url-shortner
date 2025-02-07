
from fastapi import FastAPI
from pydantic import BaseModel


class Url(BaseModel):
    url: str


app = FastAPI()

@app.post("/shorten")
async def create_url(url: Url):
    return {"message": "Hello World: from write service"}