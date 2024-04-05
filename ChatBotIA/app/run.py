from Controller.zapbot import ZapBot
from time import sleep
from View.menu import Menu
from Controller.openaiBot import Openai
from Controller.geminiBot import Gemini
from Controller.googleSearchBot import PesquisaGoogle
from Controller.testUrl import test_url

class MainApp:
    def __init__(self):
        self.openai = Openai()
        self.genai = Gemini()
        self.menu = Menu()
        self.search = PesquisaGoogle()
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
        # váriaveis das opções de totvs:
        self.retorno_totvs = ""        
        self.uslock = "" # 1
        self.sysOff = "" # 2
        self.rError = "" # 3

    def run(self):
        try:
            while True:
                sleep(2)
                nova_msg = self.bot.ultima_msg()
                if nova_msg != "sair":
                    if nova_msg is not None and nova_msg != self.msg:
                        self.msg = nova_msg
                        
                        if self.msg is not None and self.retorno_suporte == "" and self.retorno_totvs == "" and self.retorno_rede == "" and self.retorno_acessos == "":
                            
                            if self.msg == "help":
                                self.menu.show_menu()
                            elif self.msg == "sair":
                                self.menu.sair()
                            elif self.msg == "suporte":
                                self.retorno_suporte = self.menu.suporte()
                            elif self.msg == "rede":
                                self.retorno_rede = self.menu.rede()
                            elif self.msg == "acessos":
                                self.retorno_acessos = self.menu.acessos()
                            elif self.msg == "totvs":
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
                            elif self.msg == "help" or self.msg == "sair":
                                self.retorno_suporte = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                        
                        # Envia para openai a mensagem do usuário e depois envia a mensagem de resposta da openai         
                        elif self.msg is not None and self.retorno_suporte == "1" and self.imp == "1":                            
                            nova_msg = ""
                            while self.msg != "sair" and nova_msg is not None and nova_msg != self.msg:                    
                                msg = self.msg
                                resposta_openai = self.openai.iniciar_conversa(msg)
                                if resposta_openai != "":
                                    # retorna a resposta da openai
                                    self.bot.envia_msg(resposta_openai)
                                    nova_msg = self.bot.ultima_msg()
                                    self.msg = nova_msg
                        
                        # -----------------------------------------------------------------------------------------------------
                        # Caso rede mostre as opções:           
                        elif self.msg is not None and self.retorno_rede == "1" and self.netOff == "" and self.vpnOff == "" and self.pageOff == "":
                            
                            if self.msg == "1":
                                self.netOff = self.menu.net_off()
                            elif self.msg == "2":
                                self.anydesk = self.vpnOff = self.menu.vpn_off()
                            elif self.msg == "3":
                                self.page_out = self.pageOff = self.menu.page_off()
                            elif self.msg == "help" or self.msg == "sair":
                                self.retorno_rede = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                        
                        # Envia a URL para testar o site:         
                        elif self.msg is not None and self.retorno_rede == "1" and self.page_out == "1":
                            nova_msg = ""
                            while self.msg != "sair" and nova_msg is not None and nova_msg != self.msg:                    
                                msg = self.msg
                                resposta_testUrl = test_url(msg)
                                if resposta_testUrl != "":
                                    # retorna a resposta da openai
                                    self.bot.envia_msg(resposta_testUrl)
                                    nova_msg = self.bot.ultima_msg()
                                    self.msg = nova_msg
                                    
                        # -----------------------------------------------------------------------------------------------------
                        # Caso acessos mostre as opções:           
                        elif self.msg is not None and self.retorno_acessos == "1" and self.changePass == "" and self.unblockPass == "":
                            
                            if self.msg == "1":
                                self.changePass = self.menu.change_pass()
                            elif self.msg == "2":
                                self.unblockPass = self.menu.unblock_pass()
                            elif self.msg == "3":
                                self.menu.pc_nao_liga()                            
                            elif self.msg == "help" or self.msg == "sair":
                                self.retorno_suporte = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                        
                        # -----------------------------------------------------------------------------------------------------
                        # Caso totvs mostre as opções:            
                        elif self.msg is not None and self.retorno_totvs == "1" and self.rError == "":
                            
                            if self.msg == "1":
                                self.uslock = self.menu.user_lock()
                            elif self.msg == "2":
                                self.sysOff = self.menu.system_crash()
                            elif self.msg == "3":
                                self.rError = self.menu.routine_error()
                            elif self.msg == "help" or self.msg == "sair":
                                self.retorno_totvs = ""
                            else:
                                self.bot.envia_msg('Desculpe não entendi, por gentileza digite uma opção válida.')
                                
                        # Envia para gemini a mensagem do usuário e depois envia a mensagem de resposta da gemini         
                        elif self.msg is not None and self.retorno_totvs == "1" and self.rError == "1":
                            nova_msg = ""
                            while self.msg != "sair" and nova_msg is not None and nova_msg != self.msg:                    
                                msg = self.msg
                                resposta_gemini = self.genai.iniciar_conversa(msg)
                                resposta_search = self.search.enviar_pergunta(msg)
                                if resposta_gemini != "" and resposta_search != "":
                                    # retorna a resposta da openai
                                    self.bot.envia_msg(resposta_gemini)
                                    self.bot.envia_msg(resposta_search)
                                    nova_msg = self.bot.ultima_msg()
                                    self.msg = nova_msg                                
                                
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
