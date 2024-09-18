import logging

log_validations = logging.getLogger('validations')

def validate_input(model, airline, departure, arrive, flight_number):
    if not model:
        log_validations .error("Modelo do avião vazio.")
        print("O modelo do avião não pode ser vazio.")
        return False
    log_validations .debug(f"Modelo do avião: {model}")
    if  not airline:
        log_validations .error("Empresa aérea vazia.")
        print("A empresa aérea não pode ser vazia.")
        return False
    log_validations .debug(f"Empresa aérea: {airline}")
    if not departure:
        log_validations .error("Origem vazia.")
        print("A origem não pode ser vazia.")
        return False
    log_validations .debug(f"Origem: {departure}")
    if not arrive:
        log_validations .error("Destino vazio.")
        print("O destino não pode ser vazio.")
        return False
    log_validations .debug(f"Destino: {arrive}")
    if not flight_number:
        log_validations .error("Número do voo vazio.")
        print("O número do voo não pode ser vazio.")
        return False
    log_validations .debug(f"Número do voo: {flight_number}")
    return True

def validate_passengers(passengers):
    try:        
        if passengers <= 0:
            log_validations .debug(f"Número de passageiros: {passengers}")
            print("O número de passageiros deve ser positivo.")
            return False
    except ValueError:
        log_validations .error(f"{passengers}, número de passageiros inválido.")
        print("Número de passageiros inválido. Deve ser um número inteiro.")
        return False
    return True
