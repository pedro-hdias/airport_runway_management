import logging, datetime


def validate_input(model, airline, departure, arrive, flight_number):
    if not model:

        logging.error("Modelo do avião vazio.")

        print("O modelo do avião não pode ser vazio.")

        return False

    logging.debug(f"Modelo do avião: {model}")
    if  not airline:

        logging.error("Empresa aérea vazia.")

        print("A empresa aérea não pode ser vazia.")

        return False

    logging.debug(f"Empresa aérea: {airline}")
    if not departure:

        logging.error("Origem vazia.")

        print("A origem não pode ser vazia.")

        return False

    logging.debug(f"Origem: {departure}")
    if not arrive:

        logging.error("Destino vazio.")

        print("O destino não pode ser vazio.")

        return False

    logging.debug(f"Destino: {arrive}")

    if not flight_number:

        logging.error("Número do voo vazio.")

        print("O número do voo não pode ser vazio.")

        return False

    logging.debug(f"Número do voo: {flight_number}")

    return True



def validate_passengers(passengers):

    try:        

        if passengers <= 0:

            logging.debug(f"Número de passageiros: {passengers}")

            print("O número de passageiros deve ser positivo.")

            return False

    except ValueError:

        logging.error(f"{passengers}, número de passageiros inválido.")

        print("Número de passageiros inválido. Deve ser um número inteiro.")

        return False

    return True


def get_menu():
    menu_options = {
        1: "Adicionar um avião na fila de decolagem",
        2: "Permitir a decolagem do primeiro avião na fila",
        3: "Mostrar o total de aviões aguardando na fila de decolagem",
        4: "Listar todos os aviões na fila de decolagem",
        5: "Listar as características do próximo a decolar",
        6: "Mostrar a posição de um avião conforme o número do voo",
        0: "Sair"
    }
    return menu_options


def get_menu():
    menu_options = {
        1: "Adicionar um avião na fila de decolagem",
        2: "Permitir a decolagem do primeiro avião na fila",
        3: "Mostrar o total de aviões aguardando na fila de decolagem",
        4: "Listar todos os aviões na fila de decolagem",
        5: "Listar as características do próximo a decolar",
        6: "Mostrar a posição de um avião conforme o número do voo",
        0: "Sair"
    }
    return menu_options


def configure_logging():
    log_file_name = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(
        filename=log_file_name,
        filemode='a',
        format='%(funcName)s - %(levelname)s - %(message)s - %(asctime)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        encoding='utf-8',
        level=logging.DEBUG
    )
