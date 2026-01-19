from fastapi import FastAPI
from pydantic import BaseModel
from agent import app as agent_app

api = FastAPI()

class ChatRequest(BaseModel):
    message: str

@api.post("/chat")
def chat(req: ChatRequest):
    result = agent_app.invoke({
        "message": req.message
    })
    return result
