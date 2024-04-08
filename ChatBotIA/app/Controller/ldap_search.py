# ldap_search.py
import re

def search_user(connection, domain, username):
    try:
        connection.search(f"DC={domain},DC=int", f"(cn={username})")
        ou_values = ""
        for entry in connection.entries:
            match = re.search(r'OU=([^,]+)', entry.entry_dn)
            ou_values = match.group(1)
        return ou_values
    except Exception as e:
        resposta = "Erro ao buscar usuário, verifique se o login do usuário foi digitado corretamente."
        return resposta
