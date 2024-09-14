
class Aircrafts:
    """
        Class that represents an aircraft in the takeoff queue
    """

    def __init__(self, model: str, air_line: str, departure: str, arrive: str, passengers: int, flight_number: str):
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Modelo da aeronave não pode ser vazio")
        if not isinstance(air_line, str) or not air_line.strip():
            raise ValueError("Companhia aérea não pode ser vazio")
        if not isinstance(departure, str) or not departure.strip():
            raise ValueError("Origem não pode ser vazio")
        if not isinstance(arrive, str) or not arrive.strip():
            raise ValueError("Destino não pode ser vazio")
        if not isinstance(passengers, int) or passengers <= 0:
            raise ValueError("O número de passageiros deve ser um inteiro positivo.")        
        if not isinstance(flight_number, str) or not flight_number.strip():
            raise ValueError("Número do voo não pode ser vazio")
        
        self.model = model
        self.air_line = air_line
        self.departure = departure
        self.arrive = arrive
        self.passengers = passengers
        self.flight_number = flight_number

    def __str__(self):
        return f"Voo: {self.flight_number}: Aeronave: {self.model}, C&A: {self.air_line}\n Origem: {self.departure}, Destino: {self.arrive}, POB: {self.passengers}"