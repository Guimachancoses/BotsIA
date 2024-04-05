from googleapiclient.discovery import build

class URLCorrector:
    def __init__(self):
        self.api_key = ''
        self.engine_id = ''
        self.service = build("customsearch", "v1", developerKey=self.api_key)
        self.engine = self.engine_id
        

    def suggest_url(self, query):
        try:
            result = self.service.cse().list(q=query, cx=self.engine_id).execute()
            if 'items' in result:
                suggested_url = result['items'][0]['link']  # A primeira URL retornada pela pesquisa
                return suggested_url
            else:
                return None
        except Exception as e:
            print("Erro ao consultar a API do Google Custom Search:", e)
            return None

