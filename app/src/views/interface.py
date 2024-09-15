import logging
from utils.helpers import get_menu
menu_options = get_menu()

def show_menu():
    logging.debug("Exibindo o menu.")
    print("""\n===== Sistema de Gerenciamento de Fila de Decolagem =====\n
          Selecione uma opção:""")
    for key, value in menu_options.items():
        logging.debug(f"{key}. {value}")
        print(f"{key}. {value}")

def get_user_option():
    try:
        logging.debug("Obtendo a opção do usuário.")
        option = int(input("Digite o número da opção desejada: "))
        if option < 0 or option > 6:
            logging.warning(f"Opção inválida: {option}")
            print(f"Opção inválida! Por favor, insira um dos números exibidos no menu.")
            return -1
        logging.debug(f"Opção escolhida: {option}")
        return option
    except ValueError:
        logging.warning(f"Opção inválida: {option}.")
        print("Opção inválida! Por favor, insira um número.")
        return -1
