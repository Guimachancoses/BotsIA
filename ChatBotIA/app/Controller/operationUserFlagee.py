from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class FlageeOperations:
    def __init__(self, response):
        self.browser = response

    # Função para navegar em site encontrar o email do usuário:   
    def find_mail_user(self, user):
        try:
            self.browser.get("https://painel.flagee.cloud/clientarea.php?action=productdetails&id=1128&mg-page=emailAccount&modop=custom&a=management")
            sleep(30)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="accounts"]/div[1]/div[1]/div/input'))).click()
            self.email_fields = self.browser.find_element(By.XPATH, '//*[@id="accounts"]/div[1]/div[1]/div/input')
            self.email_fields.send_keys(user)
            self.email_fields.send_keys(Keys.ENTER)
            result = "Busca por email concluído!"
            return result
        except Exception as e:
            result = (f'Error na tentativa buscar o email: {user}')
            return result

    # Função para mudar o status do usuário para bloqueado:
    def change_status_user(self):
        try:
            sleep(30)
            # Aguarda o usuário aparecer:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="accounts"]/div[3]/div[1]/table/tbody/tr/td[1]/div/div/label/span')))
            # Aguarda a presença do botão de mais opções
            self.elemento_checkbox = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mg-drop-target-btn")))
            # Encontre o botão pelo seletor de classe
            self.botao = self.browser.find_element(By.CLASS_NAME, "mg-drop-target-btn")
            self.browser.execute_script("arguments[0].removeAttribute('class', 'drop-enable')", self.botao)
            # Remover display: none; do primeiro elemento
            self.browser.execute_script('document.querySelector(".mg-drop-bg-wrapper").style.removeProperty("display");')
            # Remover display: none; do segundo elemento
            self.browser.execute_script('document.querySelector(".drop").style.removeProperty("display");')
            sleep(2)
            # Agora você pode clicar em change status:
            self.browser.find_element(By.XPATH, '//*[@id="accounts"]/div[3]/div[1]/table/tbody/tr[1]/td[6]/span/div[2]/div/div/ul/li[2]/a').click()
            sleep(2)
            # Funções para tornar o select visivel:
            self.browser.find_element(By.XPATH, '//*[@id="changeStatusForm"]/div/div[1]/div[1]').click()
            # Mudar para display:block o terceiro elemento
            self.browser.execute_script('''
            var thirdElement = document.querySelector("#changeStatusForm > div > div.selectize-control.single.plugin-directionDetector");
            thirdElement.style.display = "block";
            ''')

            # Agora você pode clicar na opção "Bloqueado"
            self.browser.find_element(By.CSS_SELECTOR, "#changeStatusForm > div > div.selectize-control.single.plugin-directionDetector > div.selectize-dropdown.single.plugin-directionDetector > div > div:nth-child(2)").click()
            # Clicar em confirmar:
            sleep(1)
            self.browser.find_element(By.XPATH, '//*[@id="mgModalContainer"]/div[3]/button[1]').click()
            sleep(10)
            result = ("Status do email alterado para 'Bloqueado'!")
            return result
        except Exception as e:
            result =('Error na tentativa alterar o status do email.')
            return result
