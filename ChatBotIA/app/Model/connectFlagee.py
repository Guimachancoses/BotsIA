import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep

class FlageeConnect:
    def __init__(self):
        self.solver = recaptchaV2Proxyless()
        self.mail = os.getenv('mail_flagee')
        self.password = os.getenv('password_flagee')
        self.BrokerCp = os.getenv('brokercp')
        self.browser = None

    def start_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        # options.add_argument('--headless')

        try:
            self.browser = webdriver.Chrome(options=options)
            self.browser.implicitly_wait(5)
            if self.browser is not None:
                return self.browser
            else:
                self.browser = None
        except WebDriverException as e:
            print(f"Um erro ocorreu ao iniciar o Chrome driver.")
            exit()

    def login(self):
        try:
            self.browser.get("https://painel.flagee.cloud/login")
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]')))
            login_field = self.browser.find_element(By.XPATH, '//*[@id="inputEmail"]')
            password_field = self.browser.find_element(By.XPATH, '//*[@id="inputPassword"]')
            login_field.send_keys(self.mail)
            password_field.send_keys(self.password)

            # Resolve captcha
            self.chave_captcha = '6LfouhEjAAAAAJbiL2fcPw12KfmxL4pCL4yRYwjC'
            self.solver.set_verbose(0) # Retorna mensagem de resposta da resolução do captcha se: (1)
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
                return connection
            else:
                connection = "Error logging in!"
                sleep(15)
                return connection
        except (Exception, TimeoutError) as e:
            return"Error logging."

    def close_connection(self):
        if self.browser is not None:
            self.browser.quit()
            return "Connection closed successfully!"
