import pyttsx3
import speech_recognition as sr
import openai
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Criar um cliente OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Síntese de fala para o Chatbot =====================================
def speak_chatbot(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Número de palavras por minuto
    engine.setProperty('volume', 1)  # Volume, min: 0, max: 1
    print("Chatbot falando:", text)
    engine.say(text)
    engine.runAndWait()

# Reconhecimento de fala usando Microfone ============================
def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Ouvindo:')
        audio = recognizer.listen(source)
        # Salvar o áudio em um arquivo .wav
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = recognizer.recognize_google(audio, language='pt-BR')
        print('Você disse:', frase)
        return frase
    except sr.UnknownValueError:
        print("Não entendi")
        return "Não entendi"
    except sr.RequestError as e:
        print(f"Erro ao se comunicar com o serviço de reconhecimento de fala: {e}")
        return ""

# Integração com a API OpenAI =======================================
def retorna_resposta_modelo(mensagens, modelo="gpt-3.5-turbo", temperatura=0.7):
    try:
        response = client.chat.completions.create(
            model=modelo,
            messages=mensagens,  # Lista de mensagens no formato [{"role": "user", "content": "Sua mensagem"}]
            temperature=temperatura
        )
        return response.choices[0].message.content # Retornar o conteúdo da resposta
    except Exception as e:
        print(f"Erro ao se comunicar com a OpenAI: {e}")
        return "Erro ao gerar resposta"
