from Controller.zapbot import ZapBot

class Menu:
    def __init__(self):
        self.bot = ZapBot()
                
    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------MENU------------------------------------------------------------------------
    # Chama as opções do menu:
    def show_menu(self):
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos digite:
                        ⚫  suporte (para saber mais)
                        ⚫  rede (para saber mais)
                        ⚫  acessos (para saber mais)
                        ⚫  totvs (para saber mais)
                        ❌  sair (para encerrar) \n Digite uma das opções.""")
        
    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------SUPORTE---------------------------------------------------------------------
    # Caso a oção for suporte mostra:
    def suporte(self):
        suporte = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ⚫ 1  (problema com a impressora)
                        ⚫ 2  (computador não liga)
                        ⚫ 3  (instalação de software)
                        ⚫  help (voltar ao menu)
                        ❌  sair (para encerrar) \n Digite uma das opções.""")
        return suporte

    # Caso escolha em suporte for 1:
    def suporte_impressora(self):
        imp = "1"
        self.bot.envia_msg("Entendo, você está com problema na impressora. \n Qual o problema que você está enfrentando?")
        return imp

    # Caso escolha em suporte for 2:
    def pc_nao_liga(self):
        pcOff = "1"
        self.bot.envia_msg("Entendo, seu computador não está ligando.\nVou direcionálo para um de nossos técnicos.")
        return pcOff
    
    # Caso escolha em suporte for 3:
    def install_soft(self):
        installsoft = "1"
        self.bot.envia_msg("Entendo, você deseja instalar um software em sua máquina.\nVou direcionálo para um de nossos técnicos.")
        return installsoft

    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------REDE------------------------------------------------------------------------
    # Caso a oção for rede mostra:
    def rede(self):
        rede = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ⚫ 1  (sem internet)
                        ⚫ 2  (vpn não funciona)
                        ⚫ 3  (site não funciona)
                        ⚫  help (voltar ao menu)
                        ❌  sair (para encerrar) \n Digite uma das opções.""")
        return rede
    
    # Caso a escolha em rede for 1:
    def net_off(self):
        netOff = "1"
        self.bot.envia_msg("Entendo, você está sem internet vou direcionar a sua solicitação para um de nossos técnicos.")
        return netOff
    
    # Caso a escolha em rede for 1:
    def vpn_off(self):
        vpnOff = "1"
        self.bot.envia_msg("Entendo, você está acesso a VPN vou direcionar a sua solicitação para um de nossos técnicos. \nPor gentileza informe o número do seu Anydesk.")
        return vpnOff
    
    # Caso a escolha em rede for 1:
    def page_off(self):
        pageOff = "1"
        self.bot.envia_msg("Entendo, você está problemas para acessar um site. \nPor gentileza informe o link do site.")
        return pageOff

    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------ACESSOS---------------------------------------------------------------------
    # Caso a oção for acessos mostra:
    def acessos(self):
        acesssos = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ⚫ 1  (troca de senha)
                        ⚫ 2  (desbloqueio ou liberação)
                        ⚫ 3  (bloqueio de usuário)
                        ⚫  help (voltar ao menu)
                        ❌  sair (para encerrar)\n Digite uma das opções.""")
        return acesssos
    
    # Caso a escolha em acessos for 1:
    def change_pass(self):
        changePass = "1"
        self.bot.envia_msg("Entendo, você deseja aterar sua seunha.\nPor gentileza informe qual a plataforma que você deseja efetuar a troca de senha.")
        return changePass
    
    # Caso a escolha em acessos for 2:
    def unblock_pass(self):
        unblockPass = "1"
        self.bot.envia_msg("Entendo, você deseja aterar sua seunha.\nPor gentileza informe qual a plataforma que você deseja efetuar a troca de senha.")
        return 
    
    # Caso a escolha em acessos for 3:
    def block_user1(self):
        blockUser = "1"
        self.bot.envia_msg("Entendo, você deseja bloquear um usuário.\nEssa função requer um nível de usuário.\nPor gentileza informe seu nome completo.")
        return blockUser
    
    def block_user2(self):
        blockUser2 = "1"
        self.bot.envia_msg("Agora informe sua senha.")
        return blockUser2
       
    def block_user3(self):
        blockUser3 = "1"
        self.bot.envia_msg("Informe o nome completo do usuário que você deseja bloquear.")
        return blockUser3
    
    def block_user4(self):
        blockUser4 = "1"
        self.bot.envia_msg("Informe o motivo que você deseja bloquear o usuário.")
        return blockUser4
    
    def block_user5(self):
        blockUser5 = "1"
        self.bot.envia_msg("""Certo, se você deseja agendar um bloqueio?
                            \nDigite 'agendar'.
                            \nOu se você deseja bloquear o usuário agora?
                            \nDigite 'bloquear'.""")
        return blockUser5
    
    def block_user6(self):
        blockUser6 = "1"
        self.bot.envia_msg("Entendo, para agendar um bloqueio.\nVou encaminhar sua solicitação para o setor do T.I.")
        return blockUser6
    
    def block_user7(self):
        blockUser7 = "1"
        self.bot.envia_msg("Certo, todas as.\nVou encaminhar sua solicitação para o setor do T.I.")
        return blockUser7

    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------TOTVS-----------------------------------------------------------------------
    # Caso a oção for Totvs mostra:
    def totvs(self):
        totvs = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ⚫ 1  (usuário preso)
                        ⚫ 2  (sistema travado)
                        ⚫ 3  (erro na rotina)
                        ⚫  help (voltar ao menu)
                        ❌  sair (para encerrar)\n Digite uma das opções.""")
        return totvs
    
    # Caso escolha em suporte for 1:
    def user_lock(self):
        uslock = "1"
        self.bot.envia_msg("""Entendo, você está com seu usuário preso. 
                           \nVou encaminhar seu problema para um de nossos técnicos. 
                           \nPara poder reestabelecer o seu acesso é necessário reiniciar o nosso servidor da Totvs. 
                           \nPara isso peço a sua compreensão.
                           \nTempo mínimo para resolução do seu problema 6 horas. 
                           \nCaso exeda o tempo abra um chamado para o setor do T.I.""")
        return uslock

    # Caso escolha em suporte for 2:
    def system_crash(self):
        sysOff = "1"
        self.bot.envia_msg("Entendo, o sistema está travado vou direcioná-lo para um de nossos técnicos, para que possamos entender melhor o seu problema.")
        return sysOff
    
    # Caso escolha em suporte for 1:
    def routine_error(self):
        rError = "1"
        self.bot.envia_msg("Entendo, você está com problema em uma das rotinas do Protheus. \nMe fale qual o problema que você está enfrentando? \nEm qual rotina e qual modulo?")
        return rError

    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------SAIR------------------------------------------------------------------------
    # Caso a oção for sair mostra:
    def sair(self):
        self.bot.envia_msg("Obrigado até a próxima!")
        return False
