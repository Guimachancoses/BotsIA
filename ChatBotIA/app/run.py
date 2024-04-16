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
from View.mainFlagee import mainFlagee
from View.openTicket import mainTiflux
import re


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
        self.userNameContato, self.userFoneContato = self.bot.get_data_user()
        self.bot.envia_msg(f"⚡⛑ Olá, {self.userNameContato}. Sou Guilherme! Para receber ajuda digite: help ⛑⚡")
        self.imagem = self.bot.dir_path + "/Python-Programs/botOpenai/app/image.jpg"
        self.msg = ""
        # váriaveis das opções de suporte:        
        self.retorno_suporte = ""
        self.imp = "" # 1
        self.installSoft = "" # 3
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
        # variáveis do contato
        self.mailUserContato = ""
        self.titleTicket = ""
        self.description = []


    def run(self):
        try:
            while True:
                sleep(2)

                self.msg = self.get_new_msg()
                if self.msg != "Aguardando nova mensagem...":
                    # -----------------------------------------------------------------------------------------------------
                    # Mostra MENU principal:
                    if self.retorno_suporte == "" and self.retorno_totvs == "" and self.retorno_rede == "" and self.retorno_acessos == "":
                        
                        self.exibe_menu(self.msg)
                    
                    # -----------------------------------------------------------------------------------------------------
                    # Caso SUPORTE mostre as opções:           
                    elif self.retorno_suporte == "1" and self.imp == "" and self.installSoft == "":
                        
                        self.exibe_submenu_suporte(self.msg)
                            
                    # Caso opção 1, envia para openai a mensagem do usuário e depois envia a mensagem de resposta da openai         
                    elif self.retorno_suporte == "1" and self.imp == "1": 
                                                    
                        self.enviar_openai(self.msg)                          
                    
                    # Caso opção 3, pergunta ao usuário qual sistema ele quer instalar:         
                    elif self.retorno_suporte == "1" and self.installSoft == "1":
                        
                        self.op_install_soft(self.msg)                                            
                                                                
                    # -----------------------------------------------------------------------------------------------------
                    # Caso REDE mostre as opções:           
                    elif self.retorno_rede == "1" and self.netOff == "" and self.vpnOff == "" and self.pageOff == "":
                        
                        self.exibe_submenu_rede(self.msg)
                    
                    # Envia a URL para testar o site:         
                    elif self.retorno_rede == "1" and self.page_out == "1":
                        
                        self.testar_url(self.msg)
                        # self.titleTicket = str('Chamado aberto via bot: Opção "Rede - Categoria: Site indisponível".' - CASO CHAMADO
                                
                    # -----------------------------------------------------------------------------------------------------
                    # Caso ACESSOS mostre as opções:           
                    elif self.retorno_acessos == "1" and self.changePass == "" and self.unblockPass == "" and self.blockUser == "":
                        
                        self.exibe_submenu_acessos(self.msg)
                            
                    # Caso opção 3 "Bloqueio usuário"
                    elif self.retorno_acessos == "1" and self.blockUser == "1":
                        
                        self.bloqueio_usuario(self.msg)                                 
                                            
                    # -----------------------------------------------------------------------------------------------------
                    # Caso TOTVS mostre as opções:            
                    elif self.retorno_totvs == "1" and self.rError == "":
                        
                        self.exibe_submenu_totvs(self.msg)
                            
                    # Envia para gemini a mensagem do usuário e depois envia a mensagem de resposta da gemini         
                    elif self.retorno_totvs == "1" and self.rError == "1":
                        
                        self.envia_gemini(self.msg)
                        
                    # -----------------------------------------------------------------------------------------------------
                    # Caso NENHUMA DAS OPÇÕES mostre: 
                    else:
                        self.menu.nenhuma_op()

                    
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
            
            
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
    # Função pega nova mensagem:        
    def get_new_msg(self):
        self.nova_msg = self.bot.ultima_msg()
        if (self.nova_msg != "sair" or self.nova_msg != "Sair"):
            if self.nova_msg is not None and self.nova_msg != self.msg:
                self.msg = self.nova_msg
                return self.msg
            else:
                return "Aguardando nova mensagem..."
        else:
            self.menu.sair()
            return False        
            
            
    # função caso a escolha seja instalar software:
    def op_install_soft(self, msg):
        self.msg = msg
        self.nova_msg = ""
        while (self.msg != "sair" or self.msg != "Sair") and self.nova_msg is not None and self.nova_msg != self.msg:
            self.pergunta = self.bot.ultima_msg()                                
            if self.pergunta != "" and self.pergunta is not None:
                self.escolha_soft = self.pergunta
                self.ret_intallSoft = self.menu.install_soft2
                self.conct_description = str(self.ret_intallSoft + self.escolha_soft)
                self.description.append(self.conct_description)
                self.nova_msg = self.bot.ultima_msg()
                self.msg = self.nova_msg


    # Função para exibier submenu caso opção totvs:
    def exibe_submenu_totvs(self, msg):
        self.msg = msg
        if self.msg == "1":
            self.uslock = self.menu.user_lock()
            self.titleTicket = str('Chamado aberto via bot: Opção "Totvs - Categoria: Limite de conexão do usuário".')
        elif self.msg == "2":
            self.sysOff = self.menu.system_crash()
            self.titleTicket = str('Chamado aberto via bot: Opção "Totvs - Categoria: Sistema travado".')
        elif self.msg == "3":
            self.rError = self.menu.routine_error()
        elif ((self.msg).lower()) == "help" or self.msg == "sair":
            self.retorno_totvs = ""
            self.msg = ""
        else:
            self.menu.nenhuma_op()
            
            
    # Função para exibir submenu de acessos:
    def exibe_submenu_acessos(self, msg):
        self.msg = msg
        if self.msg == "1":
            self.changePass = self.menu.change_pass()
            self.titleTicket = str('Chamado aberto via bot: Opção "Acessos - Categoria: Troca de senha".')
        elif self.msg == "2":
            self.unblockPass = self.menu.unblock_pass()
            self.titleTicket = str('Chamado aberto via bot: Opção "Acessos - Categoria: Desbloquio | Liberação".')
        elif self.msg == "3":
            self.blockUser = self.menu.block_user1()                            
        elif ((self.msg).lower()) == "help" or self.msg == "sair":
            self.retorno_suporte = ""
            self.msg = ""
        else:
            self.menu.nenhuma_op()
            
            
    # Função para exibir o submenu de rede:
    def exibe_submenu_rede(self, msg):
        self.msg = msg
        if self.msg == "1":
            self.netOff = self.menu.net_off()
            self.titleTicket = str('Chamado aberto via bot: Opção "Rede - Categoria: Sem acesso a internet".')
        elif self.msg == "2":
            self.anydesk = self.vpnOff = self.menu.vpn_off()
            self.titleTicket = str('Chamado aberto via bot: Opção "Rede - Categoria: Sem acesso a VPN".')
        elif self.msg == "3":
            self.page_out = self.pageOff = self.menu.page_off()
        elif ((self.msg).lower()) == "help" or self.msg == "sair":
            self.retorno_rede = ""
            self.msg = ""
        else:
            self.menu.nenhuma_op()

    
    
    # Função exibir submenu de Suporte:
    def exibe_submenu_suporte(self, msg):
        self.msg = msg
        if self.msg == "1":
            self.imp = self.menu.suporte_impressora()
        elif self.msg == "2":
            self.pcOff = self.menu.pc_nao_liga()
            self.description.append(self.pcOff)
            self.titleTicket = str('Chamado aberto via bot: Opção "Suporte - Categoria: Computador não liga".')
            self.condicao_op_chamado()
        elif self.msg == "3":
            self.installSoft = self.menu.install_soft()
            self.titleTicket = str('Chamado aberto via bot: Opção "Suporte - Categoria: Intalar software".')
        elif ((self.msg).lower()) == "help" or self.msg == "sair":
            self.retorno_suporte = ""
            self.msg = ""
        else:
            self.menu.nenhuma_op()
            
            
    # Função exibir Menu:
    def exibe_menu(self, msg):
        if ((msg).lower()) == "help":
            self.menu.show_menu()
        elif ((msg).lower()) == "sair":
            self.menu.sair()
        elif ((msg).lower()) == "suporte":
            self.retorno_suporte = self.menu.suporte()
        elif ((msg).lower()) == "rede":
            self.retorno_rede = self.menu.rede()
        elif ((msg).lower()) == "acessos":
            self.retorno_acessos = self.menu.acessos()
        elif ((msg).lower()) == "totvs":
            self.retorno_totvs = self.menu.totvs()
        else:
            self.menu.nenhuma_op()
            
            
    # Função para enviar a Gemini
    def envia_gemini(self, msg):
        self.msg = msg
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
                
                
    # Função para enviar para a OpenAI
    def enviar_openai(self, msg):
        self.msg = msg
        self.nova_msg = ""
        while (self.msg != "sair" or self.msg != "Sair") and self.nova_msg is not None and self.nova_msg != self.msg:                    
            if self.attemps <= 2:
                self.pergunta = self.bot.ultima_msg()
                if self.pergunta != "" and self.pergunta is not None:
                    self.msg_op = self.pergunta
                    self.description.append(self.msg_op)
                    self.resposta_openai = self.openai.iniciar_conversa(self.msg_op)
                    if self.resposta_openai != "":
                                            # retorna a resposta da openai
                        self.bot.envia_msg(self.resposta_openai)
                        sleep(5)
                        self.choiseImp = self.menu.redirect2()
                        if "Sim" in self.choiseImp:
                            self.menu.redirect3()
                            self.menu.redirect()
                            self.CValues.cleanAll()
                            self.nova_msg = self.bot.ultima_msg()
                            self.msg = self.nova_msg
                        else:
                            self.menu.redirect4()
                            self.attempts =+ 1
                            self.pergunta = ""
            else:
                self.nova_msg = ""
                self.menu.redirect5()
                self.menu.get_mail()
                while (self.msg != "sair" or self.msg != "Sair") and self.nova_msg is not None and self.nova_msg != self.msg:  
                    self.mailUserContato = self.bot.ultima_msg()
                    if self.mailUserContato != "":
                        self.titleTicket = str('Chamado aberto via bot: Opção "Suporte - Categoria: Impressora".')
                        self.condicao_op_chamado()
                        
                
    # Funão para Testar URL:
    def testar_url(self, msg):
        self.msg = msg
        self.nova_msg = ""
        while self.msg != "sair" and self.nova_msg is not None and self.nova_msg != self.msg:                    
            self.msg_link = self.msg
            self.resposta_testUrl = test_url(self.msg_link)
            if self.resposta_testUrl != "":
                                    # retorna a resposta da do teste
                self.bot.envia_msg(self.resposta_testUrl)
                self.nova_msg = self.bot.ultima_msg()
                self.msg = self.nova_msg
                
                
    # FUnção para Bloquear usuário:
    def bloqueio_usuario(self, msg):
        self.msg = msg
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
                    self.menu.msg_wait()                                      
                    if self.connection is not None:
                        self.path = search_user(self.connection, self.domain, self.user)
                        if self.path != "Erro ao buscar usuário, verifique se o login do usuário foi digitado corretamente.":
                            if self.username != self.user:
                                self.resposta = desable_selected_user(self.connection, self.domain, self.user, self.path)
                                mainFlagee(self.user)
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
    
    
    # Função para abertura de Ticket:
    def condicao_op_chamado(self):
        if self.titleTicket != "" and len(self.description) != 0:
            if self.mailUserContato == "":
                self.menu.get_mail()
                self.nova_msg = ""
                while (self.msg.lower() != "sair") and (self.nova_msg is not None) and (self.nova_msg != self.msg):
                    self.nova_msg2 = self.bot.ultima_msg()
                    if (self.nova_msg2 != "sair" or self.nova_msg2 != "Sair"):
                        if self.nova_msg2 is not None and self.nova_msg2 != self.msg:
                            self.mailUserContato = self.nova_msg2
                            if self.verificar_email(self.mailUserContato):
                                if self.mailUserContato != "" and self.mailUserContato is not None:
                                    if self.userNameContato != "" or self.userFoneContato != "":
                                        self.op_ticket(self.userNameContato, self.mailUserContato, self.userFoneContato, self.titleTicket, self.description)
                                    else:
                                        self.userNameContato, self.userFoneContato = self.bot.get_data_user()
                                        self.op_ticket(self.userNameContato, self.mailUserContato, self.userFoneContato, self.titleTicket, self.description)
                            else:
                                self.menu.get_mail2()
                                self.mailUserContato = ""
                                self.nova_msg2 = ""
            else:
                self.op_ticket(self.userNameContato, self.mailUserContato, self.userFoneContato, self.titleTicket, self.description)
        
        
    # Se todas as variaveis estiverem presente ABRE TICKET:        
    def op_ticket(self, userNameContato, mailUserContato, userFoneContato, titleTicket, description):
        
        mainTiflux(userNameContato, mailUserContato, userFoneContato, titleTicket, description)
        self.menu.op_ticket()                              
        self.menu.redirect()
        self.CValues.cleanAll()
        self.nova_msg = self.bot.ultima_msg()
        self.msg = self.nova_msg
    
    
    # Verifica se email foi digitado como esperado:    
    def verificar_email(self, email):
        # Expressão regular para validar o formato do email
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(regex, email):
            return True
        else:
            return False

            
def main():
    # Crie uma instância de MainApp e execute o método run
    app = MainApp()
    app.run()

if __name__ == "__main__":
    main()
