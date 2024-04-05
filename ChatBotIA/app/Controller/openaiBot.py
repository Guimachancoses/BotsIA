import openai

class Openai:
    def __init__(self):
        self.key = ''
        self.api_key = self.key
        openai.api_key = self.key

    def enviar_mensagem(self, mensagem, lista_mensagens=[]):
        lista_mensagens.append(
            {"role": "user", "content": mensagem}
        )
        
        resposta = openai.chat.completions.create(
            model = "gpt-4",
            messages = lista_mensagens,
        )
        
        return resposta.choices[0].message.content

    def iniciar_conversa(self, mensagem):
        listaMensagens = [
            {"role": "system", "content": "You are a helpful assistant designed to answer simple questions in no more than 10 words about printer problems."},
        ]            
        resposta = self.enviar_mensagem(mensagem, listaMensagens)
        listaMensagens.append(resposta)
        
        if len(resposta.split()) > 10:
            return "Aguarde,um dos nossos técnicos irá lhe atender."
        else:
            return resposta
