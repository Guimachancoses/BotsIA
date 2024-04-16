from Controller.operationTiflux import OperationTiflux
from Model.connectTiflux import TifluxConnect
    

class OpenTicketTiflux:
    
    def __init__(self, browser):
        self.browser = browser
        self.cnn = OperationTiflux(self.browser)
        
    # Função abrir ticket    
    def open_ticket(self, user, email, fone, title, description=[]):
        self.user = user
        self.email = email
        self.fone = fone
        self.title = title
        self.listDescription = description
        
        
        try:
            # Prencher todos os campos do ticket:
            # Campo do nome:
            self.sendName = self.cnn.fill_name(self.cnn, self.user)
            if self.sendName is True:
                self.sendEmail = self.cnn.fill_email(self.cnn, self.email)
                if self.sendEmail is True:
                    self.sendFone = self.cnn.fill_fone(self.cnn, self.fone)
                    if self.sendFone is True:
                        self.sendTitle = self.cnn.fill_title(self.cnn, self.title)
                        if self.sendTitle is True:
                            for self.description in self.listDescription:
                                self.sendDescription = self.cnn.fill_description(self.cnn, self.description)
                            if self.sendDescription is True:
                                self.resolveCaptcha = self.cnn.resolve_captcha(self.cnn)
                                if "Task solved!" in self.resolveCaptcha:
                                    self.sendAll = self.cnn.send_all(self.cnn)
                                    if self.sendAll is True:
                                        print("Ticket abriu com sucesso!")                                        
                                    else:
                                        print("Erro ao abrir ticket")
                                else:
                                     print("Erro ao resolver o captcha")
                            else:
                                print("Erro ao preencher a descrição")
                        else:
                            print("Erro ao preencher o título")
                    else:
                        print("Erro ao preencher o fone")
                else:
                    print("Erro ao preencher o email")
            else:
                print("Erro ao preencher o nome")
        except Exception as e:
            print("Error: ", e)

# Função Main:
def mainTiflux(user, email, fone, title, description=[]):
        try:
            cnn = TifluxConnect()
            browser = cnn.start_browser(cnn)
            oTicket = OpenTicketTiflux(browser)
            oTicket.open_ticket(user, email, fone, title, description)
        except Exception as e:
            print("Error: ", e)
        finally:
            cnn.close_connection(cnn, browser)
# if __name__ == "__main__":
#     mainTiflux()