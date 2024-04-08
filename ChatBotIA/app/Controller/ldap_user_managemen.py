# ldap_user_management.py
from ldap3 import MODIFY_REPLACE

def is_user_disabled(connection, domain, username):
    try:
        connection.search(f"DC={domain},DC=int", f"(cn={username})", attributes=['userAccountControl'])
        for entry in connection.entries:
            user_account_control = int(entry.userAccountControl.value)
            if (user_account_control & 514) == 514:
                return True
        return False
    except Exception as e:
        print(f"Erro ao verificar o status do usuário {username}: {str(e)}")
        return False

def disable_user(connection, domain, username, path):
    try:
        if is_user_disabled(connection, domain, username):
            resposta = f"Usuário {username} já está desabilitado."
            return resposta
        else:
            value_modifier = 514
            connection.modify(f"CN={username},OU={path},DC={domain},DC=int", {'userAccountControl': [(MODIFY_REPLACE, [f'{value_modifier}'])]})
            resposta = f"Usuário {username} desabilitado com sucesso."
        return resposta
    except Exception as e:
        resposta = f"Erro ao desabilitar usuário {username}: {str(e)}"
        return resposta
