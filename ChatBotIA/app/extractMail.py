from Model.connectFlagee import FlageeConnect
from View.executorFlagee import FlageeExecutor


def extractMail():
    while True:
        try:
            connect = FlageeConnect()
            response = connect.start_browser()
            if response is not None:
                automator = FlageeExecutor(connect, response)
                resposta = automator.run()
                if "Status do email alterado para 'Bloqueado'!" in resposta:                   
                    # print(resposta)
                    False
                    return resposta
        except Exception as e:
            resposta = (f"Error: {e}")
            False
            return resposta
    
    
    
    
# Caso for rodar separadamente, mova esse arquivo para fora da View            
if __name__ == "__main__":
  
    extractMail()
