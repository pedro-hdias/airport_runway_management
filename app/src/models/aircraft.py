import logging

class Aircraft:
    """
        Class that represents an aircraft in the takeoff queue
    """

    def __init__(self, model: str, air_line: str, departure: str, arrive: str,  flight_number: str, passengers: int):
        logging.debug(f"Criando voo: {model}, {air_line}, {departure}, {arrive}, {passengers}, {flight_number}")
        if not isinstance(model, str) or not model.strip():
            logging.error("Modelo da aeronave vazio.")
            raise ValueError("Modelo da aeronave não pode ser vazio")
        if not isinstance(air_line, str) or not air_line.strip():
            logging.error("Empresa aérea vazia.")
            raise ValueError("Companhia aérea não pode ser vazio")
        if not isinstance(departure, str) or not departure.strip():
            logging.error("Origem vazia.")
            raise ValueError("Origem não pode ser vazio")
        if not isinstance(arrive, str) or not arrive.strip():
            logging.error("Destino vazio.")
            raise ValueError("Destino não pode ser vazio")
        if not isinstance(flight_number, str) or not flight_number.strip():
            logging.error("Número do voo vazio.")
            raise ValueError("Número do voo não pode ser vazio")
        if not isinstance(passengers, int) or passengers <= 0:
            logging.error("Número de passageiros inválido.")
            raise ValueError("O número de passageiros deve ser um inteiro positivo.", passengers)        

        self.model = model
        self.air_line = air_line
        self.departure = departure
        self.arrive = arrive
        self.passengers = passengers
        self.flight_number = flight_number

    def __str__(self):
        return f"Voo: {self.flight_number}: Aeronave: {self.model}, C&A: {self.air_line}\n Origem: {self.departure}, Destino: {self.arrive}, POB: {self.passengers}"