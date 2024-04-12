from View.openTicket import OpenTicketTiflux
from Model.connectTiflux import TifluxConnect

def mainTiflux(user, email, fone, title, description):
        try:
            cnn = TifluxConnect()
            browser = cnn.start_browser(cnn)
            oTicket = OpenTicketTiflux(browser)
            oTicket.open_ticket(user, email, fone, title, description)
        except Exception as e:
            print("Error: ", e)
        finally:
            cnn.close_connection(browser)

if __name__ == "__main__":
    mainTiflux()