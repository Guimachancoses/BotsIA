from Controller.zapbot import ZapBot

class Menu:
    def __init__(self):
        self.bot = ZapBot()
                
    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------MENU------------------------------------------------------------------------
    # Chama as opções do menu:
    def show_menu(self):
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos digite:
                        ▪️  Suporte - (Para saber mais)
                        ▪️  Rede    - (Para saber mais)
                        ▪️  Acessos - (Para saber mais)
                        ▪️  Totvs   - (Para saber mais)
                        ❌ Sair     (Para encerrar) 
                        \nDigite uma das opções.""")
        
    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------SUPORTE---------------------------------------------------------------------
    # Caso a oção for suporte mostra:
    def suporte(self):
        suporte = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ▪️ 1  -  (Problema com a impressora)
                        ▪️ 2  -  (Computador não liga)
                        ▪️ 3  -  (Instalação de programa|sistema)
                        ⬅️ Help (Voltar ao menu)
                        ❌ Sair (Para encerrar) 
                        \nDigite uma das opções.""")
        return suporte

    # Caso escolha em suporte for 1:
    def suporte_impressora(self):
        imp = "1"
        self.bot.envia_msg("""Entendo, você está com problema na impressora.
                           \nQual o problema que você está enfrentando?
                           \nDigite 'Sair' a qualquer momento, caso queira encerrrar.""")
        return imp

    # Caso escolha em suporte for 2:
    def pc_nao_liga(self):
        pcOff = "Usuário: Computador | Notebook, não está ligando."
        self.bot.envia_msg("Entendo, seu computador não está ligando.\nVou direcionálo para um de nossos técnicos.")
        return pcOff
    
    # Caso escolha em suporte for 3:
    def install_soft(self):
        installsoft = "1"
        self.bot.envia_msg("Entendo, você deseja instalar um 'programa|sistema' em sua máquina.\nInforme o nome do programa.")
        return installsoft
    
    def install_soft2(self):
        installsoft2 = "Chamado aberto via Bot Whatsapp.\nUsuário solicitou a instalação de: \n"
        self.bot.envia_msg("Certo, iremos encaminhar sua solicitação ao departamento de T.I.")
        return installsoft2

    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------REDE------------------------------------------------------------------------
    # Caso a oção for rede mostra:
    def rede(self):
        rede = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ▪️ 1  -  (Sem internet)
                        ▪️ 2  -  (Vpn não funciona)
                        ▪️ 3  -  (Site não funciona)
                        ⬅️ Help (Voltar ao menu)
                        ❌ Sair (Para encerrar) 
                        \nDigite uma das opções.""")
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
                        ▪️ 1   -  (Troca de senha)
                        ▪️ 2   -  (Desbloqueio ou liberação)
                        ▪️ 3   -  (Bloqueio de usuário)
                        ⬅️ Help (Voltar ao menu)
                        ❌ Sair (Para encerrar)
                        \nDigite uma das opções.""")
        return acesssos
    
    # Caso a escolha em acessos for 1:
    def change_pass(self):
        changePass = "1"
        self.bot.envia_msg("Entendo, você deseja aterar sua senha.\nPor gentileza informe qual a plataforma que você deseja efetuar a troca de senha?")
        return changePass
    
    # Caso a escolha em acessos for 2:
    def unblock_pass(self):
        unblockPass = "1"
        self.bot.envia_msg("Entendo, você precisa de desbloqueio ou liberação.\nPor gentileza informe qual a plataforma que você deseja pedir um desbloqueio ou liberação?.")
        return unblockPass
    
    # Caso a escolha em acessos for 3:
    def block_user1(self):
        blockUser = "1"
        self.bot.envia_msg("""Entendo, você deseja bloquear um usuário.
                           \nEssa função requer um nível de usuário administrador de rede.
                           \nPor gentileza informe seu usuário de login a rede.""")
        return blockUser
    
    def block_user2(self):
        blockUser2 = "1"
        self.bot.envia_msg("Certo, agora informe sua senha.\nNão se preocupe sua senha não será armazenada nos registros dessa conversa.")
        return blockUser2
       
    def block_user3(self):
        blockUser3 = "1"
        self.bot.envia_msg("Informe o login do usuário que você deseja bloquear (Conforme o login do AD).")
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

    def block_user8(self):
        blockUser8 = "1"
        self.bot.envia_msg("""Atenção, se você deseja bloquear um usuário.
                           \nEssa função requer um nível de usuário administrador de rede.
                           \nPor gentileza informe seu usuário de login a rede.""")
        return blockUser8

    def error_block(self):
        errorBlock = "1"
        self.bot.envia_msg("""Sinto muito, parece que você não possui credenciais de administrador de rede.
                            \nProcure o sertor do T.I.
                            \nOu escolha a opção de agendar bloqueio de usuário.""")
        return errorBlock
    
    def msg_clean(self):
        msgClean = "1"
        self.bot.envia_msg("Pronto, já apagamos sua senha da nossa conversa.\nVocê também pode apagar caso você queira.")
        return msgClean
    
    def msg_wait(self):
        msgWait = "1"
        self.bot.envia_msg("Aguarde estamos bloqueando os acessos do usuario...")
        return msgWait
    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------TOTVS-----------------------------------------------------------------------
    # Caso a oção for Totvs mostra:
    def totvs(self):
        totvs = "1"
        self.bot.envia_msg("""GuiBot: Esse é um texto com os comandos válidos:
                        ▪️ 1  -   (Usuário preso)
                        ▪️ 2  -   (Sistema travado)
                        ▪️ 3  -   (Erro na rotina)
                        ⬅️ Help (Voltar ao menu)
                        ❌ Sair (Para encerrar)
                        \nDigite uma das opções.""")
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
        self.bot.envia_msg("""Entendo, você está com problema em uma das rotinas do Protheus. 
                           \nMe fale qual o problema que você está enfrentando? 
                           \nEm qual rotina e qual modulo?""")
        return rError

    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------SAIR------------------------------------------------------------------------
    # Caso a oção for sair mostra:
    def sair(self):
        self.bot.envia_msg("Obrigado até a próxima!")
        return False
    
    #--------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------REDIRECT--------------------------------------------------------------------
    # Caso a opção for sair mostra:
    # Mensagem antes de redirecionar o usuário:
    def redirect(self):
        redirect = 1
        self.bot.envia_msg("""Você será redirecionado para o menu principal, caso desejar continuar!
                           \nSe não digite 'Sair' para encerrar a qualquer momento.""")
        return redirect
    
    # Mensagem identificar se a resposta ajudou o usuário:
    def redirect2(self):
        redirect2 = 1
        self.bot.envia_msg("""Essa informação foi útil?
                           \nDigite 'Sim' ou 'Não'.""")
        return redirect2
    
    # Mensagem identificar se a resposta ajudou o usuário, caso sim:
    def redirect3(self):
        redirect3 = 1
        self.bot.envia_msg("Que bom, que pude lhe ajudar!")
        return redirect3
    
    # Mensagem identificar se a resposta ajudou o usuário, caso sim:
    def redirect4(self):
        redirect4 = 1
        self.bot.envia_msg("""Me desculpe, você deseja fazer outra pergunta?
                           \nCaso 'Sim' envie sua nova pergunta.
                           \nOu 'Sair' para encerrar a qualquer momento.""")
        return redirect4
    
    # Mensagem identificar se a resposta ajudou o usuário, caso sim:
    def redirect6(self):
        redirect6 = 1
        self.bot.envia_msg("""Certo, por gentileza informe seu problema novamente.
                           \nSe puder detalhar melhor, para que eu possa entender a sua necessidade.
                           \nDigite 'Sair' para encerrar a qualquer momento.""")
        return redirect6
    
    def redirect5(self):
        redirect5 = 1
        self.bot.envia_msg("""Me desculpe, infelizmente não consegui te ajudar.
                           \nVou encaminhar seu problema para o setor do T.I.""")
        return redirect5
    
    def get_mail(self):
        getMail = 1
        self.bot.envia_msg("Por gentileza informe seu email, assim manteremos contato.")
        return getMail
    
    def get_mail2(self):
        getMail2 = 1
        self.bot.envia_msg("Por gentileza informe um email, válido.")
        return getMail2
    
    def op_ticket(self):
        opTicket = 1
        self.bot.envia_msg("Um chamado foi aberto, um de nossos técnicos entrará em contato.")
        return opTicket
    
    def nenhuma_op(self):
        nenhuma_op = 1
        self.bot.envia_msg("Desculpe não entendi, você não digitou nenhuma opção válida, tente novamente.")
        return nenhuma_op
    
        
