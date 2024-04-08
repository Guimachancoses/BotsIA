# ldap_connection.py
from ldap3 import Connection, Server

class LDAPManager:
    def __init__(self):
        self.host = '192.168.0.250'
        self.domain = 'garbuio'
        self.server = Server(self.host, get_info=True, use_ssl=True, tls=None)
        self.connection = None

    def connect(self, username, password):
        try:
            self.connection = Connection(self.server, user=f"{self.domain}\\{username}", password=password, auto_bind=True)
            resposta = "Conexão com o AD estabelecida com sucesso."
            return self.connection, self.domain, resposta
        except Exception as e:
            resposta = "Erro ao conectar, verifique suas credenciais."
            return self.connection, self.domain, resposta

    def disconnect(self):
        try:
            self.connection.unbind()
            resposta = "Desconectado com sucesso."
            return resposta
        except Exception as e:
            resposta = "Erro ao desconectar."
            return resposta
