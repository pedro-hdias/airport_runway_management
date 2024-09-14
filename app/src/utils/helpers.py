import logging

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