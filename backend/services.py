from backend.conversations import salvar_mensagens, ler_mensagens, listar_conversas
from backend.comunication import retorna_resposta_modelo

def process_message(user_input):
    mensagens = [{"role": "user", "content": user_input}]
    resposta = retorna_resposta_modelo(mensagens)
    mensagens.append({"role": "assistant", "content": resposta})
    salvar_mensagens(mensagens)
    return resposta

def get_conversations():
    return listar_conversas()
