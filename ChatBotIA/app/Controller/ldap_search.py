# ldap_search.py
import re
from unidecode import unidecode

def format_username(full_name):
    # Remover acentos
    normalized_name = unidecode(full_name)
    # Dividir o nome completo em partes
    parts = normalized_name.split()
    # Se houver apenas um nome, retornar sem alterações
    if len(parts) == 1:
        return normalized_name.lower()
    # Pegar o primeiro nome e o último sobrenome
    formatted_name = parts[0] + parts[-1]
    # Transformar em minúsculas
    formatted_name = formatted_name.lower()
    return formatted_name


def search_user(connection, domain, username):
    try:           
        usernameFormat = username
        usernameJoin = format_username(usernameFormat)
        connection.search(f"DC={domain},DC=int", f"(sAMAccountName={usernameJoin})")
        ou_values = ""
        for entry in connection.entries:
            match = re.search(r'OU=([^,]+)', entry.entry_dn)
            ou_values = match.group(1)
        if ou_values == '':
            usernameFull = username
            connection.search(f"DC={domain},DC=int", f"(cn={usernameFull})")
            ou_values = ""
            for entry in connection.entries:
                match = re.search(r'OU=([^,]+)', entry.entry_dn)
                ou_values = match.group(1)
        return ou_values
    except Exception as e:
        resposta = "Erro ao buscar usuário, verifique se o login do usuário foi digitado corretamente."
        return resposta
    
