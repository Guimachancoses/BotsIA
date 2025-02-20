from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class FlageeOperationsFindMails:
    def __init__(self, response):
        self.browser = response

    # Função para navegar em site encontrar o email do usuário:   
    def find_mail_user(self):
        try:
            self.browser.get("https://painel.flagee.cloud/clientarea.php?action=productdetails&id=1128&mg-page=emailAccount&modop=custom&a=management")
            sleep(30)
            # Esperar carregamento da tabela
            WebDriverWait(self.browser, 30).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@id="accounts"]/div[3]/div[1]/table/tbody/tr')
                )
            )

            # Encontrar todos os elementos de email
            email_elements = self.browser.find_elements(
                By.XPATH, '//*[@id="accounts"]/div[3]/div[1]/table/tbody/tr/td[1]/div/span'
            )

            # Extrair textos e armazenar em uma lista
            emails = [element.text.strip() for element in email_elements if element.text]

            print("Emails encontrados:", emails)
            return emails

        except Exception as e:
            print(f"Erro ao buscar emails: {e}")
            return []

    