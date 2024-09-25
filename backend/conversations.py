import pickle
from pathlib import Path

PASTA_MENSAGENS = Path(__file__).parent / 'mensagens'
PASTA_MENSAGENS.mkdir(exist_ok=True)

def salvar_mensagens(mensagens):
    nome_arquivo = 'conversa_atual'
    with open(PASTA_MENSAGENS / nome_arquivo, 'wb') as f:
        pickle.dump(mensagens, f)

def ler_mensagens():
    with open(PASTA_MENSAGENS / 'conversa_atual', 'rb') as f:
        return pickle.load(f)

def listar_conversas():
    return [f.stem for f in PASTA_MENSAGENS.glob('*')]
