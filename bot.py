from openai import OpenAI #Importando uma biblioteca da openAI
from dotenv import load_dotenv #Importar bilbioteca para leiturar do arquivo .env
import os #Para chamar a biblioteca load_dotenv precisa dessa parte

load_dotenv() #Função de py para carregar o dotenv

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def bot(enviar_mensagem):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Um vendedor de laranja que vende somente laranja, é estremamente rude e rispido"},
            {"role": "user", "content": enviar_mensagem}
        ]
    )
    return completion.choices[0].message.content
while True:

    enviar_mensagem = input("Pergunte: ")
    if enviar_mensagem.lower() == 'sair':
        print("Chat enecerrado")
        break

    reposta = bot(enviar_mensagem)
    print(reposta)