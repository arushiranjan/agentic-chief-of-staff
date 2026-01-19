from fastapi import FastAPI
from pydantic import BaseModel

from agent import app as agent_app
from db import init_db

api = FastAPI()

# ✅ Create tables on startup
@api.on_event("startup")
def startup_event():
    init_db()

class ChatRequest(BaseModel):
    message: str

@api.post("/chat")
def chat(req: ChatRequest):
    result = agent_app.invoke({
        "message": req.message
    })
    return result
