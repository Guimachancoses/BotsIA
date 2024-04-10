import openai
import os

class Openai:
    def __init__(self):
        self.api_key = os.getenv('key_openai')
        self.key = self.api_key
        self.api_key = self.key
        openai.api_key = self.key

    def enviar_mensagem(self, mensagem, lista_mensagens=[]):
        lista_mensagens.append(
            {"role": "user", "content": mensagem}
        )
        
        resposta = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = lista_mensagens,
        )
        
        return resposta.choices[0].message.content

    def iniciar_conversa(self, mensagem):
        listaMensagens = [
            {"""role": "system", "content": "Você é um assistente útil Brasileiro projetado para responder a perguntas simples em no máximo 20 palavras sobre problemas de impressora.
             Em português do Brasil. Caso a pergunta não for relacionado a problemas com a impressora, retorne 'Desculpe, não tenho essa informação.'."""},
        ]            
        resposta = self.enviar_mensagem(mensagem, listaMensagens)
        listaMensagens.append(resposta)
        
        if len(resposta.split()) > 30:
            return "Aguarde,um dos nossos técnicos irá lhe atender."
        else:
            return resposta
