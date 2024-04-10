import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep
import os

class FlageeAutomator:
    def __init__(self):
        self.mail = os.getenv('mail_flagee')
        self.password = os.getenv('password_flagee')
        self.BrokerCp = os.getenv('brokercp')
        self.browser = None
        self.solver = recaptchaV2Proxyless()    
        
    
    def start_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        # options.add_argument('--headless')

        try:
            self.browser = webdriver.Chrome(options=options)
            self.browser.implicitly_wait(5)
        except WebDriverException as e:
            print(f"An error occurred while starting Chrome driver: {e}")
            exit()

    def login(self):
        try:
            self.browser.get("https://painel.flagee.cloud/login")
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]')))
            login_field = self.browser.find_element(
                By.XPATH, '//*[@id="inputEmail"]')
            password_field = self.browser.find_element(
                By.XPATH, '//*[@id="inputPassword"]')
            login_field.send_keys(self.mail)
            password_field.send_keys(self.password)

            # Resolve captcha
            self.chave_captcha = '6LfouhEjAAAAAJbiL2fcPw12KfmxL4pCL4yRYwjC'
            self.solver.set_verbose(1) # Retorna mensagem de resposta da resolução do captcha
            self.solver.set_key(self.BrokerCp) # Chave da API do captcha
            self.solver.set_website_url(self.browser.current_url) # Passa a URL do site
            self.solver.set_website_key(self.chave_captcha) # Define a chave do site
            self.resposta = self.solver.solve_and_return_solution()

            if self.resposta != 0:
                # Id JSON 'g-recaptcha-response'
                self.browser.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML ='{self.resposta}'")
                # Clica no botão de login
                sleep(4)
                self.browser.find_element(By.CLASS_NAME, 'button03').click()
                sleep(5)
                connection = "Logged in successfully!"            
                return self.browser
            else:
                connection = "Error logging in!"
                sleep(15)
                return self.browser
        except (Exception, TimeoutError) as e:
            print (f"Error logging in{e}")
            
    # Função para navegar em site encontrar o email do usuário:
    def find_mail_user(self, user):
        try:
            self.browser.get("https://painel.flagee.cloud/clientarea.php?action=productdetails&id=1128&mg-page=emailAccount&modop=custom&a=management")
            sleep(2)
            # Altera a URL para o link absoluto da lista dos email:
            expected_url = "https://painel.flagee.cloud/login"
            # Obtém a URL atual do navegador:
            current_url = self.browser.current_url
            # Verifica se a URL atual corresponde à URL esperada
            if expected_url in current_url:
                # Se a URL não estiver correta, faz o login novamente:
                self.login()
            else:
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
            print("Status do email alterado para 'Bloqueado'!")
        except Exception as e:
            print(f'Error na tentativa alterar o status do email:{e}')
            
    
    def run(self,user):
        try:
            self.start_browser()
            self.response = self.login()
            if self.response == "Logged in successfully!":
                self.seach_user = self.find_mail_user(user)
                if self.seach_user == 'Busca por email concluído!':
                    self.change_status_user()
                else:
                    print ("Finalizando.")
                    self.browser.quit()
                    exit()
        except Exception as e:
            print(f'Error: {e}')
            traceback.print_exc()
        finally:
            if self.browser:
                self.browser.quit()

def main():
    user = 'ederson'
    automator = FlageeAutomator()
    automator.run(user)


if __name__ == "__main__":
    main()
