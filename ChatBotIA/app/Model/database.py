import mysql.connector

class Database:
    def __init__(self):
        self.connection = self.conectar_banco_dados()

    @staticmethod
    def conectar_banco_dados():
        """Conecta ao banco de dados MySQL e retorna a conexão."""
        try:
            # Conecta ao banco de dados
            connection = mysql.connector.connect(
                host="host",
                user="user",
                password="password",
                database="db_name"
            )
            return connection
        except mysql.connector.Error as err:
            print("Erro ao conectar ao banco de dados MySQL:", err)
            return None
    
    @staticmethod
    def desconectar_banco_dados(connection):
        """Desconecta do banco de dados MySQL."""
        try:
            if connection.is_connected():
                connection.close()
                print("Conexão fechada.")
        except mysql.connector.Error as err:
            print("Erro ao fechar conexão:", err)

    def __del__(self):
        if self.connection.is_connected():
            self.desconectar_banco_dados(self.connection)
