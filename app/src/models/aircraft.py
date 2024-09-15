import logging
from utils.validations import validate_input, validate_passengers

log_aircraft = logging.getLogger('aircraft')

class Aircraft:
    """
        Class that represents an aircraft in the takeoff queue
    """

    def __init__(self, model: str, air_line: str, departure: str, arrive: str,  flight_number: str, passengers: int):
        log_aircraft.debug(f"Criando voo: {model}, {air_line}, {departure}, {arrive}, {passengers}, {flight_number}")
        if not isinstance(model, str) or not model.strip():
            log_aircraft.error("Modelo da aeronave vazio.")
            raise ValueError("Modelo da aeronave não pode ser vazio")
        if not isinstance(air_line, str) or not air_line.strip():
            log_aircraft.error("Empresa aérea vazia.")
            raise ValueError("Companhia aérea não pode ser vazio")
        if not isinstance(departure, str) or not departure.strip():
            log_aircraft.error("Origem vazia.")
            raise ValueError("Origem não pode ser vazio")
        if not isinstance(arrive, str) or not arrive.strip():
            log_aircraft.error("Destino vazio.")
            raise ValueError("Destino não pode ser vazio")
        if not isinstance(flight_number, str) or not flight_number.strip():
            log_aircraft.error("Número do voo vazio.")
            raise ValueError("Número do voo não pode ser vazio")
        if not isinstance(passengers, int) or passengers <= 0:
            log_aircraft.error("Número de passageiros inválido.")
            raise ValueError("O número de passageiros deve ser um inteiro positivo.", passengers)        

        self.model = model
        self.air_line = air_line
        self.departure = departure
        self.arrive = arrive
        self.passengers = passengers
        self.flight_number = flight_number

    def __str__(self):
        return f"Voo: {self.flight_number}: Aeronave: {self.model}, C&A: {self.air_line}\n Origem: {self.departure}, Destino: {self.arrive}, POB: {self.passengers}"

    @classmethod
    def create_aircraft(cls):
        log_aircraft.debug("Criando um novo voo.")
        print("\n=== Adicionar Avião ===")
        model = input("Modelo do avião: ").strip()
        airline = input("Empresa aérea: ").strip()
        departure = input("Origem: ").strip()
        arrive = input("Destino: ").strip()
        flight_number = input("Número do voo: ").strip()

        while True:
            try:
                passengers = int(input("Número de passageiros: "))
                break
            except ValueError:
                print("Por favor, insira um número válido de passageiros.")

        if not validate_input(model, airline, departure, arrive, flight_number):
            print("Erro ao criar o voo. Verifique os dados e tente novamente.")
            return
        if not validate_passengers(passengers):
            print("Erro ao criar o voo. O número de passageiros deve ser um inteiro positivo.")
            return

        log_aircraft.debug(f"Voo criado: {model}, {airline}, {departure}, {arrive}, {flight_number}, {passengers}")
        return cls(model, airline, departure, arrive, flight_number, passengers)
