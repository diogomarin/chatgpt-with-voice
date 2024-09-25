from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router as chat_router

app = FastAPI()

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "API para ChatGPT Replica com reconhecimento de voz"}
