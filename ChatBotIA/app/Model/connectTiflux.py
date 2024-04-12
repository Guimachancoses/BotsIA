import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep

class TifluxConnect:
    def __init__(self):
        self.solver = recaptchaV2Proxyless()
        self.BrokerCp = os.getenv('brokercp')
        self.wDrive = WebDriverWait
        self.by = By
        self.ec = EC
        self.sleep = sleep
        self.browser = None

    # Função para conecção do webdriver
    @staticmethod
    def start_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        # options.add_argument('--headless')
        try:
            self.browser = webdriver.Chrome(options=options)
            self.browser.implicitly_wait(5)
            if self.browser is not None:
                self.browser.get("https://central.tiflux.com.br/r/externals/tickets/new/3aa2d6da09887613520201a9e460c267016c8c15")
                return self.browser
            else:
                self.browser = None
        except WebDriverException as e:
            print(f"Um erro ocorreu ao iniciar a página de chamados.")

    # Função para desconecção do webdriver
    @staticmethod
    def close_connection(self):
        if self.browser is not None:
            self.browser.quit()
            return "Connection closed successfully!"
