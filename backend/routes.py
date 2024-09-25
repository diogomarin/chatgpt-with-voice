from fastapi import APIRouter, WebSocket
from pydantic import BaseModel
from backend.services import process_message, get_conversations

router = APIRouter()

# Definir um modelo Pydantic para o corpo da solicitação
class MessageInput(BaseModel): 
    user_input: str

@router.post("/send-message/")
async def send_message(input: MessageInput):
    response = process_message(input.user_input)
    return {"response": response}

@router.get("/conversations/")
async def list_conversations():
    return get_conversations()

@router.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = process_message(data)
        await websocket.send_text(response)