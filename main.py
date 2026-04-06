from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

from agent import process_query

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def home():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))


@app.get("/chat")
def chat(user_input: str):
    try:
        return process_query(user_input)
    except Exception as e:
        return {"error": str(e)}