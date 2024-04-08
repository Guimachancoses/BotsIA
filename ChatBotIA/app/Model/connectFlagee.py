import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep
import os


class FlageeAutomator:
    def __init__(self):
        self.mail = os.getenv('mail_flagee')
        self.password = os.getenv('password_flagee')
        self.browser = None
        self.solver = recaptchaV2Proxyless()
        self.solver.set_verbose(1)
        self.solver.set_key(chave_api)
        

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
        # Resolve captcha recebe link do site:
        self.solver.set_website_url(self.browser)
        # cria variavel com a captcha:
        self.chave_captcha = self.browser.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')
        # website resolve captcha:
        self.solver.set_website_key(self.chave_captcha)
        # retorno da resposta do website:
        self.resposta = self.solver.solve_and_return_solution()

        if self.resposta != 0:
            # clica no botão de login:
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div/div/form/div/div[5]/input').click()
        print("Logged in successfully!")
        sleep(15)

    # def navigate_to_queues(self):
    #     try:
    #         WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(
    #             (By.XPATH, '//*[@id="app-container"]/div[1]/div/div/nav/ul/app-nav-item[2]/a'))).click()
    #         print("Navigated to queues!")
    #     except Exception as e:
    #         print(f'Error navigating to queues: {e}')

    # def force_user_on_queue(self):
    #     try:
    #         input_field_xpath = '/html/body/div/div/div/div[2]/div[2]/div[2]/extension-list/div/div[2]/div/div[3]/div[1]/input'
    #         self.browser.find_element(By.XPATH, input_field_xpath).clear()
    #         self.browser.find_element(
    #             By.XPATH, '//*[@id="app-container"]/div[1]/div/div/nav/ul/app-nav-item[2]/a').click()
    #         sleep(1)
    #         self.browser.find_element(
    #             By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "mc-select", " " ))]//i').click()
    #         self.browser.find_element(By.XPATH, '//*[(@id = "btnStatus")]').click()
    #         sleep(15)
    #         self.browser.find_element(
    #             By.XPATH, '/html/body/div[1]/div/div/div/div[2]/select[2]/option[3]').click()
    #         sleep(1)
    #         self.browser.find_element(
    #             By.XPATH, '/html/body/div[1]/div/div/div/div[1]/button').click()
    #         sleep(1)
    #         self.browser.find_element(
    #             By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "mc-select", " " ))]//i').click()
    #         print("User forced on queue successfully!")
    #     except Exception as e:
    #         print(f'Error forcing user on queue: {e}')
    #         traceback.print_exc()

    # def change_status(self):
    #     try:
    #         userList = ['5078', '5002', '5071', '5020', '5051', '1021', '5077',
    #                     '6009', '5062', '5022', '5009', '5075', '5064', '1005', '5030', '5024', '6010', '5074',
    #                     '5055', '5093', '5069']
    #         input_field_xpath = '/html/body/div/div/div/div[2]/div[2]/div[2]/extension-list/div/div[2]/div/div[3]/div[1]/input'

    #         for user in userList:
    #             self.browser.find_element(By.XPATH, input_field_xpath).clear()
    #             self.browser.find_element(By.XPATH, input_field_xpath).send_keys(user)
    #             sleep(1)
    #             self.browser.find_element(
    #                 By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/extension-list/div/div[2]/div/div[3]/table/tbody/tr/td[1]/label/i').click()
    #             self.browser.find_element(By.XPATH, '//*[(@id = "btnStatus")]').click()
    #             sleep(5)
    #             self.browser.find_element(
    #                 By.XPATH, '/html/body/div[1]/div/div/div/div[2]/select[1]/option[2]').click()
    #             sleep(1)
    #             self.browser.find_element(
    #                 By.XPATH, '/html/body/div[1]/div/div/div/div[1]/button').click()
    #             sleep(1)
    #             print(f"Extension {user} status changed successfully!")
    #     except Exception as e:
    #         print(f'Error changing extension {user} status: {e}')
    #         traceback.print_exc()

    # def navigate_to_extensions(self):
    #     self.browser.get('https://garbuio.my3cx.com.br/#/app/system_status/all')
    #     print("Navigated to extensions!")

    def run(self):
        try:
            self.start_browser()
            self.login()
            # while True:
            #     now = datetime.datetime.now()
            #     self.navigate_to_queues()
            #     self.force_user_on_queue()

            #     current_time = now.time()
            #     print(current_time)
            #     if (current_time >= datetime.time(8, 0) and current_time <= datetime.time(12, 0)) or \
            #             (current_time >= datetime.time(13, 0) and current_time <= datetime.time(18, 0)):
            #         self.change_status()

            #     self.navigate_to_extensions()

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
