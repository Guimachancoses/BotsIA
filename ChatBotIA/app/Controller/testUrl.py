from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from fuzzywuzzy import process
import ping3
import subprocess
from Controller.customSearch import URLCorrector


class URLValidator:
    def __init__(self):
        self.corrector = URLCorrector()
        pass

    def is_invalid_url(self, url):
        try:
            parsed_url = urlparse(url)
            if not all([parsed_url.scheme, parsed_url.netloc]):  
                return True  # Retorna True se a URL não estiver no formato correto
            
            # Verifica se o domínio está respondendo ao ping
            if not self.ping_domain(parsed_url.netloc):
                return True
            
            response = requests.get(url)
            response.raise_for_status()  
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Lógica para testar se a URL é inválida
            if self.has_error_message(soup) or self.has_specific_code(response):
                return True
            return False
            
        except (requests.exceptions.RequestException, Exception):
            return True  # Se ocorrer uma exceção ao acessar a URL, considera-se inválida

    def has_error_message(self, soup):
        # Lista de códigos de erro HTTP comuns
        common_error_codes = [401, 403, 404, 500, 504]
        
        # Verifica se a página contém um código de erro HTTP comum
        for code in common_error_codes:
            if soup.find('meta', attrs={'http-equiv': f'{code}'}):
                return True
        
        # Se nenhum dos códigos de erro comuns for encontrado, retornar False
        return False

    def has_specific_code(self, response):
        # Códigos de erro específicos que você está procurando
        specific_error_codes = [400, 401, 404]  # Exemplo de códigos de erro específicos
        
        # Verifica se a resposta contém um código de erro específico
        if response.status_code in specific_error_codes:
            return True
        
        # Se nenhum código de erro específico for encontrado, retorna False
        return False
    
    def ping_domain(self, domain):
        try:
            # Verifica se o domínio está respondendo ao ping
            ping_response = ping3.ping(domain, timeout=2)
            if ping_response is None:
                return False
            return True
        except Exception:
            return False

    def trace_domain(self, domain):
        try:
            # Executa tracert para o domínio com um tempo limite de 5 segundos
            tracert_response = subprocess.run(['tracert', '-d', domain], capture_output=True, text=True, timeout=5)
            # Verifica se há resposta
            if 'Tracing route' in tracert_response.stdout:
                return True
            return False
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            return False
        
        
def test_url(url):
    validator = URLValidator()

    if validator.is_invalid_url(url):
        resposta = "A URL é inválida."
        # Verifica se o domínio está respondendo ao ping
        if not validator.ping_domain(urlparse(url).netloc):
            noPing = "\nEssa url não está respondendo a verificação."
            if noPing:
                resposta += f" {noPing}"
        else:
            isPing = "\nEssa url está respondendo a verificação."
            if isPing:
                resposta += f" {isPing}"

        # Executa tracert para o domínio e verifica se há resposta
        if not validator.trace_domain(urlparse(url).netloc):
            noTracert = "\nNão foi possível rastrear a url."
            if noTracert:
                resposta += f" {noTracert}"
        else:
            isTracert = "\nRastreamento da url bem-sucedido."
            if isTracert:
                resposta += f" {isTracert}"
        suggest = validator.corrector.suggest_url(url)
        if suggest:
            resposta += f"\nTente acessar por esse link: {suggest}"
        return resposta
    else:
        resposta = "A URL é válida."

        # Verifica se o domínio está respondendo ao ping
        if not validator.ping_domain(urlparse(url).netloc):
            noPing = "\nEssa url não está respondendo a verificação."
            if noPing:
                resposta += f" {noPing}"
        else:
            isPing = "\nEssa url está respondendo a verificação."
            if isPing:
                resposta += f" {isPing}"

        # Executa tracert para o domínio e verifica se há resposta
        if not validator.trace_domain(urlparse(url).netloc):
            noTracert = "\nNão foi possível rastrear a url."
            if noTracert:
                resposta += f" {noTracert}"
        else:
            isTracert = "\nRastreamento da url bem-sucedido."
            if isTracert:
                resposta += f" {isTracert}"
        return resposta

# Exemplo de uso da função run com uma URL inserida manualmente
# url = input("Insira a URL que você quer testar: ")
# resposta = test_url(url)
# print(resposta)

