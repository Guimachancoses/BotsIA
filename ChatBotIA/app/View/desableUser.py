# main.py
from Model.ldap_connection import LDAPManager
from Controller.ldap_search import search_user
from Controller.ldap_user_managemen import disable_user
import getpass

ldap_manager = LDAPManager()

def get_credentials():
    username = input("Digite o nome de usuário: ").strip().lower()
    password = getpass.getpass("Digite a senha: ").strip()
    return username, password

def get_search_on_user(connection, domain):
    if connection is not None:
        user = input("Digite o nome de usuário: ").strip()
        search_result = search_user(connection, domain, user)
        return user, search_result

def desable_selected_user(connection, domain, user, resposta):
    if resposta is not None:
            resultado = disable_user(connection, domain, user, resposta)
    return resultado

# Caso quiser rodar separado criar arquivo:
# main_functions.py
# from Model.ldap_connection import LDAPManager
# from View.desableUser import get_search_on_user, desable_selected_user, get_credentials

# if __name__ == "__main__":
#     ldap_manager = LDAPManager()
#     username, password = get_credentials()
#     connection, domain, resposta = ldap_manager.connect(username, password)
#     print(resposta)
#     if connection is not None:
#         user, path = get_search_on_user(connection, domain)
#         resposta_desbilitar = desable_selected_user(connection, domain, user, path)
#         print(resposta_desbilitar)
#     ldap_manager.disconnect()




