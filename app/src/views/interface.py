import logging
from utils.helpers import get_menu

menu_options = get_menu()
log_interface = logging.getLogger('interface')

def show_menu():
    log_interface.debug("Exibindo o menu.")
    print("""\n===== Sistema de Gerenciamento de Fila de Decolagem =====\n
          Selecione uma opção:""")
    for key, value in menu_options.items():
        log_interface.debug(f"{key}. {value}")
        print(f"{key}. {value}")

def get_user_option():
    try:
        log_interface.debug("Obtendo a opção do usuário.")
        option = int(input("Digite o número da opção desejada: "))
        if option < 0 or option > 6:
            log_interface.warning(f"Opção inválida: {option}")
            print(f"Opção inválida! Por favor, insira um dos números exibidos no menu.")
            return -1
        log_interface.debug(f"Opção escolhida: {option}")
        return option
    except ValueError:
        log_interface.warning("Opção inválida. Não foi inserido um número.")
        print("Opção inválida! Por favor, insira um número.")
        return -1
