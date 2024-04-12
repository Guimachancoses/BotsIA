from Model.connectTiflux import TifluxConnect

class OperationTiflux(TifluxConnect):
    
    def __init__(self, browser):
        super().__init__()
        self.browser = browser

    @staticmethod
    # Função para resolver o Captcha:
    def resolve_captcha(self):
        try:
            self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.CLASS_NAME, 'ant-btn-primary')))
            # Resolve captcha
            self.chave_captcha = '6Lf0DHwUAAAAAAC78DNwQlw0XTDSEv_mymh9iesK' # Id key for captcha do google
            self.solver.set_verbose(1) # Retorna mensagem de resposta da resolução do captcha se: (1)
            self.solver.set_key(self.BrokerCp) # Chave da API do captcha
            self.solver.set_website_url(self.browser.current_url) # Passa a URL do site
            self.solver.set_website_key(self.chave_captcha) # Define a chave do site
            self.resposta = self.solver.solve_and_return_solution()

            if self.resposta != 0:
                # Id JSON 'g-recaptcha-response'
                self.browser.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML ='{self.resposta}'")
                connection = "Task solved!"
                return connection
            else:
                connection = "Error in task solved"
                return connection
        except (Exception, TimeoutError) as e:
            return"Error logging"
    
    @staticmethod    
    # Função para preencher nome do solicitante:
    def fill_name(self, user):
        try:
            self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.ID, 'service_desk_pre_ticket_requestor_name')))
            self.browser.find_element(self.by.ID, 'service_desk_pre_ticket_requestor_name').send_keys(user)
            print("Nome preenchido.")
            return True
        except Exception as e:
            print("Error ao preencher o name: ", e)
            return False
    
    @staticmethod
    # Função para preencher email do solicitante:
    def fill_email(self, email):
        try:
            self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.ID, 'service_desk_pre_ticket_requestor_email')))
            self.browser.find_element(self.by.ID, 'service_desk_pre_ticket_requestor_email').send_keys(email)
            print("Email preenchido.")
            return True
        except Exception as e:
            print("Error ao preencher o email: ", e)
            return False
    
    @staticmethod    
    # Função para preencher fone do solicitante:
    def fill_fone(self, fone):
        try:
            self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.ID, 'service_desk_pre_ticket_requestor_telephone')))
            self.browser.find_element(self.by.ID, 'service_desk_pre_ticket_requestor_telephone').send_keys(fone)
            print("Fone preenchido.")
            return True
        except Exception as e:
            print("Error ao preencher o fone: ", e)
            return False
    
    @staticmethod    
    # Função para preencher title do chamado:
    def fill_title(self, title):
        try:
            self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.ID, 'service_desk_pre_ticket_title')))
            self.browser.find_element(self.by.ID, 'service_desk_pre_ticket_title').send_keys(title)
            print("Título preenchido.")
            return True
        except Exception as e:
            print("Error ao preencher o title: ", e)
            return False
    
    @staticmethod    
    # Função para preencher a descrição do chamado:
    def fill_description(self, description):
        try:
            self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.CLASS_NAME, 'jodit-wysiwyg')))
            self.browser.find_element(self.by.XPATH, '//*[@id="root"]/div/div/form/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]').send_keys({description})
            self.browser.execute_script(f"document.querySelector('.ace_text-input').innerHTML ='{description}'")
            # self.browser.find_element(self.by.CLASS_NAME, 'jodit-wysiwyg').send_keys(description)
            print("Conteudo do chamado preenchido.")
            return True
        except Exception as e:
            print("Error ao preencher o conteudo do chamado: ", e)
            return False
   
    # @staticmethod 
    # # Função para enviar anexo:
    # def fill_description(self, anexo):
    #     try:
    #         self.wDrive(self.browser, 20).until(self.ec.presence_of_element_located((self.by.CLASS_NAME, 'ant-upload')))
    #         self.browser.execute_script('document.querySelector("#root > div > div > form > div:nth-child(4) > div:nth-child(3) > div > div:nth-child(1) > span > div > span > input[type=file]").style.removeProperty("display");')
    #         #envia o caminho para o input
    #         self.browser.find_element(self.by.CSS_SELECTOR, '#root > div > div > form > div:nth-child(4) > div:nth-child(3) > div > div:nth-child(1) > span > div > span > input[type=file]").style.removeProperty("display");').send_keys(anexo)
    #         print("Conteudo do chamado preenchido.")
    #         return True
    #     except Exception as e:
    #         print("Error ao preencher o conteudo do chamado: ", e)
    #         return False
    
    @staticmethod
    # Função clicar no botão do enviar chamado preenchido:    
    def send_all(self):
        try:
            self.browser.find_element(self.by.CLASS_NAME, 'ant-btn-primary').click()
            self.sleep(5)
            self.close_connection()
            print("Chamado aberto!")
            return True
        except Exception as e:
            print("Erro ao abrir chamado: ", e)
            return False