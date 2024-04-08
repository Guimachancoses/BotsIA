# main_functions.py
from Model.ldap_connection import LDAPManager
from View.desableUser import get_search_on_user, desable_selected_user, get_credentials

if __name__ == "__main__":
    ldap_manager = LDAPManager()
    username, password = get_credentials()
    connection, domain, resposta = ldap_manager.connect(username, password)
    print(resposta)
    if connection is not None:
        user, path = get_search_on_user(connection, domain)
        resposta_desbilitar = desable_selected_user(connection, domain, user, path)
        print(resposta_desbilitar)
    ldap_manager.disconnect()