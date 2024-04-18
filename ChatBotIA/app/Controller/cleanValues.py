class CleanValues:
    def __init__(self):
        self.variaveis={'nova_msg':"",'msg': "",'retorno_suporte': "", 'retorno_totvs': "", 'retorno_rede': "",'retorno_acessos': "",
                   'imp': "", 'msgOp': "", 'resposta_openai': "", 'msg_link': "", 'resposta_testUrl': "",
                   'page_out': "", 'netOff': "", 'anydesk': "", 'vpnOff': "", 'changePass': "", 'unblockPass': "",
                   'blockUser': "", 'username': "",'password': "", 'user': "", 'attemps': 0, 'motivo': "",
                   'connection': "", 'domain': "", 'resposta_conn': "",'path': "", 'resposta': "",'rError': "",
                   'uslock': "", 'sysOff': "", 'send_msg': "", 'resposta_gemini': "",'resposta_search': "",'msg_get': "",
                   'msg_new': "", 'msg_new2': "",'msg_recebida': "", 'sendOp':"",'msg_getOp': "",'get2': "",
        }
    
    def cleanAll(self):
        for variavel, valor_reset in self.variaveis.items():
            setattr(self, variavel, valor_reset)

# # Criando uma instância da classe LimpadorVariaveis
# CValues = CleanValues()

# # Usando o método limpar para limpar as variáveis
# CValues.cleanAll()

