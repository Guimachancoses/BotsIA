class CleanValues:
    def __init__(self):
        self.variaveis=['self.nova_msg', 'self.msg', 'self.retorno_suporte', 'self.retorno_totvs', 'self.retorno_rede',
                   'self.retorno_acessos', 'self.imp', 'self.msg_op', 'self.resposta_openai', 'self.msg_link', 'self.resposta_testUrl',
                   'self.page_out', 'self.netOff', 'self.anydesk', 'self.vpnOff', 'self.changePass', 'self.unblockPass', 'self.blockUser', 'self.username',
                   'self.password', 'self.user', 'self.attemps', 'self.motivo', 'self.connection', 'self.domain', 'self.resposta_conn',
                   'self.path', 'self.resposta','self.rError', 'self.uslock', 'self.sysOff', 'self.send_msg', 'self.resposta_gemini',
                   'self.resposta_search']


    def cleanAll(self):
        for variavel in self.variaveis:
            if variavel in globals():
                del globals()[variavel]

# # Criando uma instância da classe LimpadorVariaveis
# CValues = CleanValues()

# # Usando o método limpar para limpar as variáveis
# CValues.cleanAll()

