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
            sleep(4)
            connection = "Logged in successfully!"
            self.browser.get("https://painel.flagee.cloud/clientarea.php?action=productdetails&id=1128&mg-page=emailAccount&modop=custom&a=management")
            sleep(15)
            return connection
        else:
            connection = "Error logging in!"
            sleep(15)
            return connection
        
    # Função para navegar em site clica conta de email:
    def navigate_to_acconut_mail(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '//div[@class="list-group-item" and @id="ClientAreaHomePagePanels-Active_Products_Services-1"]'))).click()
            print("Acesso aos email concluído!")
        except Exception as e:
            print(f'Error na tentativa de acessar os email: {e}')
            
    # Função para navegar em site clica lista de email:
    def navigate_to_mails(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href="https://painel.flagee.cloud/clientarea.php?action=productdetails&id=1128&mg-page=emailAccount&modop=custom&a=management"]'))).click()
            print("Acesso a lista de email concluído!")
        except Exception as e:
            print(f'Error na tentativa de acessar a lista dos email: {e}')
            
    # Função para navegar em site encontrar o email do usuário:
    def find_mail_user(self, user):
        try:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="accounts"]/div[1]/div[1]/div/input'))).click()
            self.email_fields = self.browser.find_element(By.XPATH, '//*[@id="accounts"]/div[1]/div[1]/div/input')
            self.email_fields.send_keys(user)
            self.email_fields.send_keys(Keys.ENTER)
            print("Busca por email concluído!")
        except Exception as e:
            print(f'Error na tentativa buscar o email: {user}')

    # Função para mudar o status do usuário para bloqueado:
    def change_status_user(self):
        try:
            # Aguarda o usuário aparecer:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="accounts"]/div[3]/div[1]/table/tbody/tr/td[1]/div/div/label/span')))
            # Aguarda a presença do elemento
            self.elemento_checkbox = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lu-form-checkbox")))
            # Execute o JavaScript para alterar a visibilidade do checkbox
            self.browser.execute_script("arguments[0].style.display = 'block';", self.elemento_checkbox)
            sleep(2)
            # Agora você pode clicar no checkbox:
            self.browser.find_element(By.CLASS_NAME, "lu-form-checkbox").click()
            # Aguarda a box do select opções de status e clica:
            # Exibir o elemento select
            self.browser.execute_script("document.querySelector('.selectize-dropdown.single.plugin-directionDetector').style.display = 'block';")
            sleep(1)
            # Agora você pode clicar na opção "Bloqueado"
            self.browser.find_element(By.CSS_SELECTOR, ".option[data-value='bloqueado']").click()
            print("Status do email alterado para 'Bloqueado'!")
        except Exception as e:
            print(f'Error na tentativa alterar o status do email:{e}')
            
    
    def run(self):
        try:
            self.start_browser()
            self.response = self.login()
            if self.response == "Logged in successfully!":
                sleep(15)
                # self.navigate_to_acconut_mail()
                # self.navigate_to_mails()
                self.find_mail_user('ederson')
                sleep(30)
                self.change_status_user()


        except Exception as e:
            print(f'Error: {e}')
            traceback.print_exc()
        finally:
            if self.browser:
                self.browser.quit()

def main():
    automator = FlageeAutomator()
    automator.run()


if __name__ == "__main__":
    main()
