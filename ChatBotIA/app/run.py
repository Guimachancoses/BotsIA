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
        #self.bot.envia_msg(f"⚡⛑ Olá, {self.userNameContato}. Sou Guilherme! Para receber ajuda digite: help ⛑⚡")
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
                self.msg_get = self.msg_new = ""
                self.msg_get = self.get_new_msg()
                self.msg_new = self.msg_get
                if (self.msg_new != self.msg and self.msg_new != "" and self.msg_new != "Aguardando nova mensagem..."):
                    self.msg = self.msg_new
                    # -----------------------------------------------------------------------------------------------------
                    # Mostra MENU principal:
                    if self.retorno_suporte == "" and self.retorno_totvs == "" and self.retorno_rede == "" and self.retorno_acessos == "":
                        
                        self.verifica_op_menu(self.msg)
                    
                    # -----------------------------------------------------------------------------------------------------
                    # Caso SUPORTE mostre as opções:           
                    elif self.retorno_suporte == "1" and self.imp == "" and self.installSoft == "":
                        
                        self.verifica_op_submenu_suporte(self.msg)                                                                    
                                                                
                    # -----------------------------------------------------------------------------------------------------
                    # Caso REDE mostre as opções:           
                    elif self.retorno_rede == "1" and self.netOff == "" and self.vpnOff == "" and self.pageOff == "":
                        
                        self.verifica_op_submenu_rede(self.msg)                 
                                   
                    # -----------------------------------------------------------------------------------------------------
                    # Caso ACESSOS mostre as opções:           
                    elif self.retorno_acessos == "1" and self.changePass == "" and self.unblockPass == "" and self.blockUser == "":
                        
                        self.verifica_op_submenu_acessos(self.msg)
                                        
                    # -----------------------------------------------------------------------------------------------------
                    # Caso TOTVS mostre as opções:            
                    elif self.retorno_totvs == "1" and self.rError == "":
                        
                        self.verifica_op_submenu_totvs(self.msg)

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
                self.msg_recebida = self.nova_msg
                return self.msg_recebida
            else:
                return "Aguardando nova mensagem..."
        else:
            self.menu.sair()      
            


    # Função para exibier submenu caso opção totvs:
    def verifica_op_submenu_totvs(self, msg):
        self.msg = msg
        match self.msg:
            case "1":
                # Caso 1 usuário preso:
                self.uslock = self.menu.user_lock()
                self.titleTicket = str('Chamado aberto via bot: Opção "Totvs - Categoria: Limite de conexão do usuário".')
                self.description.append(self.uslock)
                self.condicao_op_chamado(self.msg)
            case "2":
                # Caso 2 sistema travado:
                self.sysOff = self.menu.system_crash()
                self.titleTicket = str('Chamado aberto via bot: Opção "Totvs - Categoria: Sistema travado".')
            case "3":
                # Caso 3 problema com rotina:
                self.rError = self.menu.routine_error()
                self.envia_gemini()
                self.titleTicket = str('Chamado aberto via bot: Opção "Totvs - Categoria: Problema na rotina do Protheus".')
            case "help":
                self.retorno_totvs = ""
            case _:
                self.menu.nenhuma_op()
            
            
            
    # Função para exibir submenu de acessos:
    def verifica_op_submenu_acessos(self, msg):
        self.msg = msg
        match self.msg:
            case "1":
                # Caso 1 mudar senha:
                self.changePass = self.menu.change_pass()
                self.titleTicket = str('Chamado aberto via bot: Opção "Acessos - Categoria: Troca de senha".')
                self.description_part1 = self.changePass
                self.nameSystem = self.what_name_system()
                self.description.append(self.nameSystem)
                self.condicao_op_chamado(self.nameSys)
            case "2":
                # Caso 2 desbloqueio ou liberação:
                self.unblockPass = self.menu.unblock_pass()
                self.titleTicket = str('Chamado aberto via bot: Opção "Acessos - Categoria: Desbloquio | Liberação".')
            case "3":
                # Caso opção 3 "Bloqueio usuário"
                self.blockUser = self.menu.block_user1()
                self.bloqueio_usuario(self.msg)
            case "help":
                self.menu.show_menu()
                self.retorno_acessos = ""                            
            case _:
                self.menu.nenhuma_op()
            
            
            
    # Função para exibir o submenu de rede:
    def verifica_op_submenu_rede(self, msg):
        self.msg = msg
        match self.msg:
            case "1":
                # Caso 1 sem acesso a rede:
                self.netOff = self.menu.net_off()
                self.titleTicket = str('Chamado aberto via bot: Opção "Rede - Categoria: Sem acesso a internet".')
            case "2":
                # Caso 2 sem acesso a vpn:
                self.anydesk = self.vpnOff = self.menu.vpn_off()
                self.titleTicket = str('Chamado aberto via bot: Opção "Rede - Categoria: Sem acesso a VPN".')
            case "3":
                # Casi 3 site não funciona:
                self.descriptionPageOff, self.pageOff = self.menu.page_off()
                self.titleTicket = str('Chamado aberto via bot: Opção "Rede - Categoria: Site indisponível".')
                self.testar_url(self.msg)
            case "help":
                self.menu.show_menu()
                self.retorno_rede = ""  
            case _:
                self.menu.nenhuma_op()

    
    
    # Função exibir submenu de Suporte:
    def verifica_op_submenu_suporte(self, msg):
        self.msg = msg
        match self.msg:
            case "1":                
                # Caso 1 problema com a impressora:
                self.imp = self.menu.suporte_impressora()            
                self.enviar_openai(self.msg)  
            case "2":
                # Caso 2 computador não liga:
                self.pcOff = self.menu.pc_nao_liga()
                self.description.append(self.pcOff)
                self.titleTicket = str('Chamado aberto via bot: Opção "Suporte - Categoria: Computador não liga".')
                self.condicao_op_chamado(self.msg)
            case "3":
                # Caso 3 instalar software:
                self.installSoft = self.menu.install_soft()
                self.titleTicket = str('Chamado aberto via bot: Opção "Suporte - Categoria: Instalar | Atualizar, software".')
                self.op_install_soft()
            case "help":
                self.retorno_suporte = ""
                self.menu.show_menu()
            case _:
                self.menu.nenhuma_op()
            
            
            
    # Função exibir Menu:
    def verifica_op_menu(self, msg):
        self.msg = ((msg).lower())
        match self.msg:
            case "help":
                # Exibe o menu principal:
                self.menu.show_menu()
            case "suporte":
                # Exibe submenu de suporte:
                self.retorno_suporte = self.menu.suporte()
            case "rede":
                # Exibe submenu de rede:
                self.retorno_rede = self.menu.rede()
            case "acessos":
                # Exibe submenu de acessos:
                self.retorno_acessos = self.menu.acessos()
            case "totvs":
                # Exibe submenu da totvs:
                self.retorno_totvs = self.menu.totvs()
            case _:
                self.menu.nenhuma_op()
            
            
            
    # Função para enviar a Gemini
    def envia_gemini(self, msg):
        self.mgsGM = msg
        while True:                  
            self.getGm = self.msg_newGm = self.sendGm =""
            self.getGm = self.get_new_msg()
            self.msg_newGm = self.getGm
            if (self.msg_newGm != self.mgsGM and self.msg_newGm != self.choises and self.msg_newGm != "" and self.msg_newGm != "Aguardando nova mensagem..."):
                self.sendGm = self.msg_newGm
                self.part1_description = ("Descrição do problema: " + self.sendGm)
                self.resposta_gemini = self.genai.iniciar_conversa(self.sendGm)
                self.resposta_search = self.search.enviar_pergunta(self.sendGm)
                if self.resposta_gemini != "" and self.resposta_search != "":
                    # retorna a resposta da openai
                    self.part2_description = (f" Resposta IA: {self.resposta_gemini},\nLinks sugeridos: {self.resposta_search}")
                    self.bot.envia_msg(self.resposta_gemini)
                    sleep(2)
                    self.bot.envia_msg(self.resposta_search)
                    sleep(10)
                    self.menu.redirect2()
                    while True:
                        self.getGm2 = self.msg_newGm2 = self.choisesGm2 =""
                        self.getGm2 = self.get_new_msg()
                        self.msg_newGm2 = self.getGm2
                        if (self.msg_newGm2 != self.sendGm and self.msg_newGm2 != self.choises and self.msg_newGm2 != "" and self.msg_newGm2 != "Aguardando nova mensagem..."):
                            self.choisesGm2 = ((self.msg_newGm2).lower())
                        if self.choiseGm2 == "Sim":
                            self.menu.redirect3()
                            self.limpa_volta_menu()
                            break
                        if self.choiseGm2 == "Não":
                            self.description.append(self.part1_description, self.part2_description)
                            self.menu.redirect5()
                            self.condicao_op_chamado(self.choiseGm2)
                            break
                        else:
                            self.menu.nenhuma_op()
                        
                    break
                    
                
                
    # Função para enviar para a OpenAI
    def enviar_openai(self, msg):
        self.msgOp = msg
        while True:
            # Iniciar variareis:
            self.msg_getOp = self.msg_newOp = self.sendOp = ""                
            self.msg_getOp = self.get_new_msg()
            self.msg_newOp = self.msg_getOp
            if (self.msg_newOp != self.sendOp and self.msg_newOp != self.msgOp and self.msg_newOp != "" and self.msg_newOp != "Aguardando nova mensagem..."):
                self.sendOp = self.msg_newOp
                self.description.append(self.sendOp)
                self.resposta_openai = self.openai.iniciar_conversa(self.sendOp)
                if self.resposta_openai != "":
                    # retorna a resposta da openai
                    self.bot.envia_msg(self.resposta_openai)
                    sleep(10)
                    self.menu.redirect2()
                    pass
                    while True:
                        self.get2 = self.msg_new2 = self.choises =""
                        self.get2 = self.get_new_msg()
                        self.msg_new2 = self.get2
                        if (self.msg_new2 != self.sendOp and self.msg_new2 != self.choises and self.msg_new2 != "" and self.msg_new2 != "Aguardando nova mensagem..."):
                            self.choises = ((self.msg_new2).lower())
                            if self.choises == "sim":
                                self.menu.redirect3()
                                self.limpa_volta_menu()
                                break
                            if self.choises == "não":
                                self.description.append(self.part1_description, self.part2_description)
                                self.menu.redirect5()
                                self.condicao_op_chamado(self.choices)
                                break
                            else:
                                self.menu.nenhuma_op()
                    break
                        
                        
                
    # Funão para Testar URL:
    def testar_url(self, msg):
        self.msgTu = msg
        while True:                   
            # Iniciar variareis:
            self.msg_getTu = self.msg_newTu = self.msg_link = self.resposta_testUrl = ""                
            self.msg_getTu = self.get_new_msg()
            self.msg_newTu = self.msg_getTu
            if (self.msg_newTu != self.msg_link and self.msg_newTu != self.msgOp and self.msg_newTu != "" and self.msg_newTu != "Aguardando nova mensagem..."):
                self.msg_link = self.msg_newTu
                if self.resposta_testUrl == "":
                    self.conct_descriptionTu = (f"{self.descriptionPageOff} + {self.msg_link}")
                    self.description.append(self.conct_descriptionTu)
                    self.resposta_testUrl = test_url(self.msg_link)
                    # retorna a resposta da do teste
                    self.bot.envia_msg(self.resposta_testUrl)
                    self.menu.redirect2()
                if self.msg_link == "Sim":
                    self.menu.redirect3()
                    self.menu.show_menu()
                    self.limpa_volta_menu()
                    break
                else:
                    self.menu.redirect5()
                    self.condicao_op_chamado(self.msg_link)
                    break
                           
                            
                
    # FUnção para Bloquear usuário:
    def bloqueio_usuario(self, msg):
        self.msg = msg
        self.nova_msg = ""
        self.username = ""
        self.password = ""
        self.user = ""
        self.motivo = ""
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
                if self.password != "" and self.user != "" and self.motivo == "" and self.user != self.msg and self.msg is not None: 
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
    
    
    
    # função caso a escolha seja instalar software:
    def op_install_soft(self, msg):
        self.msgIs = msg
        # Iniciar variareis:
        self.msg_getIs = self.msg_newIs = self.pergunta = ""                
        self.msg_getIs = self.get_new_msg()
        self.msg_newIs = self.msg_getIs
        if (self.msg_newIs != self.pergunta and self.msg_newIs != self.msgIs and self.msg_newIs != "" and self.msg_newIs != "Aguardando nova mensagem..."):
            self.pergunta = self.msg_newIs
            self.envia_num_anydesk = self.get_number_anydesk()
            self.ret_intallSoft = self.menu.install_soft2
            self.conct_description = (f"{self.ret_intallSoft} + {self.pergunta} + {self.envia_num_anydesk}")
            self.description.append(self.conct_description)
            self.condicao_op_chamado(self.numberAny)
            
            
    
    # Função para abertura de Ticket:
    def condicao_op_chamado(self, msg):
        self.msgRc = msg
        if self.titleTicket != "" and len(self.description) != 0:
            if self.mailUserContato == "":
                self.menu.get_mail()
                while True:
                    self.msg_getRc = self.msg_newRc = ""                
                    self.msg_getRc = self.get_new_msg()
                    self.msg_newRc = self.msg_getRc
                    if (self.msg_newRc != self.mailUserContato and self.msg_newRc != self.msgRc and self.msg_newRc != "" and self.msg_newRc != "Aguardando nova mensagem..."):
                        self.mailUserContato = self.msg_newRc
                        if self.verificar_email(self.mailUserContato):
                            if self.mailUserContato != "" and self.mailUserContato is not None:
                                if self.userNameContato != "" or self.userFoneContato != "":
                                    self.op_ticket(self.userNameContato, self.mailUserContato, self.userFoneContato, self.titleTicket, self.description)
                                    break
                                else:
                                    self.userNameContato, self.userFoneContato = self.bot.get_data_user()
                                    self.op_ticket(self.userNameContato, self.mailUserContato, self.userFoneContato, self.titleTicket, self.description)
                                    break
                        else:
                            self.menu.get_mail2()
                            self.mailUserContato = ""
                            self.msg_getRc = self.msg_newRc = "" 
            else:
                self.op_ticket(self.userNameContato, self.mailUserContato, self.userFoneContato, self.titleTicket, self.description)
        


    # Se todas as variaveis estiverem presente ABRE TICKET:        
    def op_ticket(self, userNameContato, mailUserContato, userFoneContato, titleTicket, description):
        
        mainTiflux(userNameContato, mailUserContato, userFoneContato, titleTicket, description)
        self.menu.op_ticket()
        self.menu.show_menu()
        self.limpa_volta_menu()



    # Função para limpar todas as variaveis e voltar ao menu principal
    def limpa_volta_menu(self):
        self.nome_variavel = ""
        self.valor_variavel = ""                    
        self.menu.redirect()
        self.CValues.cleanAll()
        self.menu.show_menu()

    
    
    # Verifica se email foi digitado como esperado:    
    def verificar_email(self, email):
        # Expressão regular para validar o formato do email
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(regex, email):
            return True
        else:
            return False
    
        
    
    # Função para pegar o número do Anydesk:
    def get_number_anydesk(self, msg):
        self.msgAny = msg
        self.description_anydesk = self.menu.number_anydesk()
        while True:
            self.msg_getAny = self.msg_newAny = self.numberAny = ""                
            self.msg_getAny = self.get_new_msg()
            self.msg_newAny = self.msg_getAny
            if (self.msg_newAny != self.msgAny and self.msg_newAny != self.msgRc and self.msg_newAny != "" and self.msg_newAny != "Aguardando nova mensagem..."):
                self.numberAny = self.msg_newAny
                self.concat_number_any = (f"{self.description_anydesk} + {self.numberAny}")
                return self.concat_number_any
            
            
    
    # Função para perguntar qual o sistema:        
    def what_name_system(self, msg):
        self.msgNsys = msg
        while True:
            self.msg_getNsys = self.msg_newNsys = self.nameSys = ""                
            self.msg_getNsys = self.get_new_msg()
            self.msg_newNsys = self.msg_getNsys
            if (self.msg_newNsys != self.msgNsys and self.msg_newNsys != self.msgRc and self.msg_newNsys != "" and self.msg_newNsys != "Aguardando nova mensagem..."):
                self.nameSys = self.msg_newNsys
                self.concat_name_sys = (f"{self.description_part1} + {self.nameSys}")
                return self.concat_name_sys


            
def main():
    # Crie uma instância de MainApp e execute o método run
    app = MainApp()
    app.run()

if __name__ == "__main__":
    main()

