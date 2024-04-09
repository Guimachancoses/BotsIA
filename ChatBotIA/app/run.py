from Controller.zapbot import ZapBot
from time import sleep
from View.menu import Menu
from Controller.openaiBot import Openai
from Controller.geminiBot import Gemini
from Controller.googleSearchBot import PesquisaGoogle
from Controller.testUrl import test_url
from Model.ldap_connection import LDAPManager
from Controller.ldap_search import search_user
from View.desableUser import desable_selected_user
from Controller.cleanValues import CleanValues

class MainApp:
    def __init__(self):
        self.openai = Openai()
        self.genai = Gemini()
        self.menu = Menu()
        self.search = PesquisaGoogle()
        self.ldap_manager = LDAPManager()
        self.CValues = CleanValues()
        self.bot = self.menu.bot
        self.bot.abre_conversa("+55 19 98228-0312")
        self.bot.envia_msg("⚡⛑ Olá, sou Guilherme! Para receber ajuda digite: help ⛑⚡")
        self.imagem = self.bot.dir_path + "/Python-Programs/botOpenai/app/image.jpg"
        self.msg = ""
        # váriaveis das opções de suporte:        
        self.retorno_suporte = ""
        self.imp = "" # 1
        # váriaveis das opções de rede:
        self.retorno_rede = ""
        self.netOff = ""
        self.vpnOff = ""
        self.pageOff = ""
        # váriaveis das opções de acessos:
        self.retorno_acessos = ""
        self.changePass = ""
        self.unblockPass = ""
        self.blockUser = ""
        # váriaveis para conexão no AD
        self.motivo = ""
        self.connection = None
        self.domain = None
        self.path = None
        self.resposta = ""
        # váriaveis das opções de totvs:
        self.retorno_totvs = ""        
        self.uslock = "" # 1
        self.sysOff = "" # 2
        self.rError = "" # 3

    def run(self):
        try:
            while True:
                sleep(2)
                self.nova_msg = self.bot.ultima_msg()
                if (self.nova_msg != "sair" or self.nova_msg != "Sair"):
                    if self.nova_msg is not None and self.nova_msg != self.msg:
                        self.msg = self.nova_msg
                        
                        if self.msg is not None and self.retorno_suporte == "" and self.retorno_totvs == "" and self.retorno_rede == "" and self.retorno_acessos == "":
                            
                            if ((self.msg).lower()) == "help":
                                self.menu.show_menu()
                            elif ((self.msg).lower()) == "sair":
                                self.menu.sair()
                            elif ((self.msg).lower()) == "suporte":
                                self.retorno_suporte = self.menu.suporte()
                            elif ((self.msg).lower()) == "rede":
                                self.retorno_rede = self.menu.rede()
                            elif ((self.msg).lower()) == "acessos":
                                self.retorno_acessos = self.menu.acessos()
                            elif ((self.msg).lower()) == "totvs":
                                self.retorno_totvs = self.menu.totvs()
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                        
                        # -----------------------------------------------------------------------------------------------------
                        # Caso suporte mostre as opções:           
                        elif self.msg is not None and self.retorno_suporte == "1" and self.imp == "":
                            
                            if self.msg == "1":
                                self.imp = self.menu.suporte_impressora()
                            elif self.msg == "2":
                                self.menu.pc_nao_liga()
                            elif self.msg == "3":
                                self.menu.install_soft()
                            elif ((self.msg).lower()) == "help" or self.msg == "sair":
                                self.retorno_suporte = ""
                                self.msg = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                        
                        # Envia para openai a mensagem do usuário e depois envia a mensagem de resposta da openai         
                        elif self.msg is not None and self.retorno_suporte == "1" and self.imp == "1":                            
                            self.nova_msg = ""
                            while (self.msg != "sair" or self.msg != "Sair") and self.nova_msg is not None and self.nova_msg != self.msg:                    
                                self.msg_op = self.msg
                                self.resposta_openai = self.openai.iniciar_conversa(self.msg_op)
                                if self.resposta_openai != "":
                                    # retorna a resposta da openai
                                    self.bot.envia_msg(self.resposta_openai)
                                    self.nova_msg = self.bot.ultima_msg()
                                    self.msg = self.nova_msg                                  
                        
                        # -----------------------------------------------------------------------------------------------------
                        # Caso rede mostre as opções:           
                        elif self.msg is not None and self.retorno_rede == "1" and self.netOff == "" and self.vpnOff == "" and self.pageOff == "":
                            
                            if self.msg == "1":
                                self.netOff = self.menu.net_off()
                            elif self.msg == "2":
                                self.anydesk = self.vpnOff = self.menu.vpn_off()
                            elif self.msg == "3":
                                self.page_out = self.pageOff = self.menu.page_off()
                            elif ((self.msg).lower()) == "help" or self.msg == "sair":
                                self.retorno_rede = ""
                                self.msg = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                        
                        # Envia a URL para testar o site:         
                        elif self.msg is not None and self.retorno_rede == "1" and self.page_out == "1":
                            self.nova_msg = ""
                            while self.msg != "sair" and self.nova_msg is not None and self.nova_msg != self.msg:                    
                                self.msg_link = self.msg
                                self.resposta_testUrl = test_url(self.msg_link)
                                if self.resposta_testUrl != "":
                                    # retorna a resposta da do teste
                                    self.bot.envia_msg(self.resposta_testUrl)
                                    self.nova_msg = self.bot.ultima_msg()
                                    self.msg = self.nova_msg
                                    
                        # -----------------------------------------------------------------------------------------------------
                        # Caso acessos mostre as opções:           
                        elif self.msg is not None and self.retorno_acessos == "1" and self.changePass == "" and self.unblockPass == "" and self.blockUser == "":
                            
                            if self.msg == "1":
                                self.changePass = self.menu.change_pass()
                            elif self.msg == "2":
                                self.unblockPass = self.menu.unblock_pass()
                            elif self.msg == "3":
                                self.blockUser = self.menu.block_user1()                            
                            elif ((self.msg).lower()) == "help" or self.msg == "sair":
                                self.retorno_suporte = ""
                                self.msg = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                                
                        # Caso opção 3 "Bloqueio usuário"
                        elif self.msg is not None and self.retorno_acessos == "1" and self.blockUser == "1":
                            self.nova_msg = ""
                            self.username = ""
                            self.password = ""
                            self.user = ""
                            self.attemps = 0 
                            while (self.msg != "sair" or self.msg != "Sair") and self.nova_msg is not None and self.nova_msg != self.msg:   
                                if self.attemps <= 2:              
                                    self.msg = self.bot.ultima_msg()
                                    if self.username == "" and self.msg is not None:                                
                                        self.username = self.bot.ultima_msg()
                                        self.msg = None
                                        self.menu.block_user2()
                                    if self.password == "" and self.username != self.msg and self.msg is not None:
                                        self.password = self.bot.ultima_msg()
                                        self.msg = None                                    
                                        self.bot.apagar_ultima_msg()
                                        sleep(2)
                                        self.menu.msg_clean()
                                        self.menu.block_user3()
                                    if self.password != "" and self.user == "" and self.password != self.msg and self.msg is not None:                              
                                        self.user = self.bot.ultima_msg()
                                        self.msg = None
                                        self.menu.block_user4() # Caso queria salvar no banco de dados
                                    if self.password != "" and self.user != "" and self.motivo == "" and self.motivo != self.msg and self.msg is not None: 
                                        self.motivo = self.bot.ultima_msg()
                                    if self.username != "" and self.password != "" and self.user != "" and self.motivo != "" and self.msg is not None: 
                                        self.connection, self.domain ,self.resposta_conn = self.ldap_manager.connect(self.username, self.password)
                                        self.bot.envia_msg(self.resposta_conn)                                        
                                        if self.connection is not None:
                                            self.path = search_user(self.connection, self.domain, self.user)
                                            if self.path != "Erro ao buscar usuário, verifique se o login do usuário foi digitado corretamente.":
                                                self.resposta = desable_selected_user(self.connection, self.domain, self.user, self.path)
                                                self.bot.envia_msg(self.resposta)
                                                self.menu.redirect()
                                                self.CValues.cleanAll()
                                                self.nova_msg = self.bot.ultima_msg()
                                                self.msg = self.nova_msg
                                                self.menu.show_menu()
                                            else:
                                                self.user = ""
                                                self.bot.envia_msg(self.path)                                                
                                        else:
                                            self.menu.block_user8()
                                            self.username = ""
                                            self.password = ""
                                        self.ldap_manager.disconnect()
                                        self.attempts =+ 1
                                else:
                                    self.menu.error_block()
                                    self.nova_msg = self.bot.ultima_msg()
                                    self.msg = self.nova_msg                                 
                                                
                        # -----------------------------------------------------------------------------------------------------
                        # Caso totvs mostre as opções:            
                        elif self.msg is not None and self.retorno_totvs == "1" and self.rError == "":
                            
                            if self.msg == "1":
                                self.uslock = self.menu.user_lock()
                            elif self.msg == "2":
                                self.sysOff = self.menu.system_crash()
                            elif self.msg == "3":
                                self.rError = self.menu.routine_error()
                            elif ((self.msg).lower()) == "help" or self.msg == "sair":
                                self.retorno_totvs = ""
                                self.msg = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                                
                        # Envia para gemini a mensagem do usuário e depois envia a mensagem de resposta da gemini         
                        elif self.msg is not None and self.retorno_totvs == "1" and self.rError == "1":
                            self.nova_msg = ""
                            while (self.msg != "sair" or self.msg != "Sair") and self.nova_msg is not None and self.nova_msg != self.msg:                    
                                self.send_msg = self.msg
                                self.resposta_gemini = self.genai.iniciar_conversa(self.send_msg)
                                self.resposta_search = self.search.enviar_pergunta(self.send_msg)
                                if self.resposta_gemini != "" and self.resposta_search != "":
                                    # retorna a resposta da openai
                                    self.bot.envia_msg(self.resposta_gemini)
                                    self.bot.envia_msg(self.resposta_search)
                                    self.nova_msg = self.bot.ultima_msg()
                                    self.msg = self.nova_msg                                
                                
                        else:
                            self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                    else:
                        print("Aguardando nova mensagem...")
                else:
                    self.menu.sair()
                    break
                    
        except TimeoutError:
            print("Ocorreu um timeout.")
            print("Reiniciando o programa em 2 minutos...")
            sleep(120)  # Espera 2 minutos
            main()
        except Exception as e:
            print("Ocorreu um erro inesperado:", e)
            print("Reiniciando o programa em 2 minutos...")
            sleep(120)  # Espera 2 minutos
            main()
        except KeyboardInterrupt:
            print("O usuário interrompeu o programa. Finalizando o programa...")
            
def main():
    # Crie uma instância de MainApp e execute o método run
    app = MainApp()
    app.run()

if __name__ == "__main__":
    main()
