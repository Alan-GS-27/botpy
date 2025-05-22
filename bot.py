from openai import OpenAI #Importando uma biblioteca da openAI
from dotenv import load_dotenv #Importar bilbioteca para leiturar do arquivo .env
import os #Para chamar a biblioteca load_dotenv precisa dessa parte

load_dotenv() #Função de py para carregar o dotenv

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def mensagem(enviar_mensagem):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": enviar_mensagem}
        ]
    )
    return completion.choices[0].message.content

print(mensagem("Quem é o prediente do Brasil?"))