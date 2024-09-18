from controllers.takeoff_queue import TakeoffQueue
from models.aircraft import Aircraft
from views.interface import show_menu, get_user_option
from utils.helpers import configure_logging, get_menu
import logging, datetime

configure_logging()
log_main = logging.getLogger('main')

takeoff_queue= TakeoffQueue()
menu_display, menu_functions = get_menu()

def main():
    while True:
        try:
            log_main.info("Iniciando o programa.")
            show_menu()
            option= get_user_option()
            log_main.debug(f"Opção escolhida: {option}")

            if option== 0:
                log_main.info("Encerrando o programa.")
                menu_functions[option]()
                break

            if option in menu_functions.keys():
                menu_functions[option]()
        except Exception as e:
            log_main.error(f"Erro inesperado: {e}")
            print(f"Erro inesperado: {e}")
            break


if __name__ == "__main__":
    main()

