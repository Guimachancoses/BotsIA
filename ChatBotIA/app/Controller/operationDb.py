from Model.database import Database

class OperacoesBancoDados(Database):
    def __init__(self):
        super().__init__()
        self.connection = self.conectar_banco_dados()

    def consultar_dados(self, query):
        """Realiza uma consulta ao banco de dados e retorna os resultados."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except self.connection.Error as err:
            print("Erro ao consultar dados:", err)
            return None
        finally:
            cursor.close()

    def inserir_dados(self, query, values):
        """Insere dados no banco de dados."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
            print("Dados inseridos com sucesso.")
        except self.connection.Error as err:
            print("Erro ao inserir dados:", err)
            self.connection.rollback()
        finally:
            cursor.close()

    def atualizar_dados(self, query, values):
        """Atualiza dados no banco de dados."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
            print("Dados atualizados com sucesso.")
        except self.connection.Error as err:
            print("Erro ao atualizar dados:", err)
            self.connection.rollback()
        finally:
            cursor.close()

    def deletar_dados(self, query, values):
        """Exclui dados do banco de dados."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
            print("Dados excluídos com sucesso.")
        except self.connection.Error as err:
            print("Erro ao excluir dados:", err)
            self.connection.rollback()
        finally:
            cursor.close()

    def __del__(self):
        self.desconectar_banco_dados(self.connection)
