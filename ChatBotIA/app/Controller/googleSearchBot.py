from googleapiclient.discovery import build
import os

api_key = os.getenv('key_gsearch')

class PesquisaGoogle:
    def __init__(self):
        self.api_key = os.getenv('key_gsearch')
        self.key = self.api_key
        self.engine_key = os.getenv('key_engineTotvs')
        self.engineID = self.engine_key
        self.service = build('customsearch', 'v1', developerKey=self.key)
        self.search_engine_id = self.engineID

    def enviar_pergunta(self, pergunta):
        # Defina a consulta de pesquisa
        query = pergunta + " Protheus Totvs"

        # Defina os parâmetros da pesquisa
        params = {
            'q': query,
            'cx': self.search_engine_id,  # ID do mecanismo de pesquisa
            'num': 3,  # Número de resultados
            'sort': 'date',  # Ordenar por data
        }

        try:
            # Execute a pesquisa
            response = self.service.cse().list(q=params['q'], cx=params['cx'], num=params['num'], sort=params['sort']).execute()

            # Extraia os links
            links = [result['link'] for result in response.get('items', [])]

            # Verifique se a pesquisa está relacionada à Totvs
            if 'Protheus' not in query:
                resposta = "Desculpe, não tenho essa informação."
            else:
                resposta = "\n\nLinks da Central de Atendimento Totvs:\n" + "\n".join(links)

        except Exception as e:
            resposta = f"Ocorreu um erro ao processar sua pergunta: {str(e)}"

        return resposta

# # Inicialize a classe PesquisaGoogle
# pesquisa = PesquisaGoogle()

# # Digitar a pergunta
# pergunta = input("Digite sua pergunta: ")

# # Enviar pergunta e obter resposta
# resposta = pesquisa.enviar_pergunta(pergunta)
# print(resposta)