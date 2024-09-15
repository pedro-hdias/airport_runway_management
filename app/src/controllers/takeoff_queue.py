from collections import deque
from models.aircraft import Aircraft
import logging

log_takeoff_queue = logging.getLogger('takeoff_queue')
class TakeoffQueue:
    """
        Class that manages the aircraft takeoff queue.
    """

    def __init__(self):
        self.queue = deque()

    def add_flight(self):
        log_takeoff_queue .info("Adicionando um voo à fila de decolagem.")
        flight  = Aircraft.create_aircraft()
        log_takeoff_queue .debug(f"Adicionando avião à fila de decolagem: {flight}")
        self.queue.append(flight)

    def takeoff_flight(self):
        log_takeoff_queue .info("Decolando um voo.")
        if self.queue:
            log_takeoff_queue .debug(f"Decolando o voo: {self.queue[0]}")
            return self.queue.popleft()
        else:
            log_takeoff_queue .warning("Fila de decolagem vazia.")
            print("Não há voos na fila de decolagem.")
            return None

    def get_queue_size(self):
        log_takeoff_queue .info("Obtendo o tamanho da fila de decolagem.")
        print(f"Total de voos na fila de decolagem: {len(self.queue)}")
        log_takeoff_queue .debug(f"Tamanho da fila de decolagem: {len(self.queue)}")
        return len(self.queue)

    def get_list_all_aircraft(self):
        log_takeoff_queue .info("Listando todos os aviões na fila de decolagem.")
        if len(self.queue) == 0:
            print("A fila de decolagem está vazia.")
            log_takeoff_queue .warning("Tentativa de listar aviões com fila vazia.")
            return None
        else:
            print("\n=== Voos na Fila de Decolagem ===")
            for idx, flight in enumerate(self.queue, start=1):
                print(f"{idx}. {flight}")

    def get_next_aircraft(self):
        log_takeoff_queue .info("Obtendo o próximo avião na fila de decolagem.")
        if self.queue:
            log_takeoff_queue .debug(f"Próximo avião na fila: {self.queue[0]}")
            print(f"Próximo avião a decolar: {self.queue[0]}")
            return self.queue[0]
        else:
            log_takeoff_queue .warning("Fila de decolagem vazia.")
            print("Não há voos na fila de decolagem.")
            return None

    def get_aircraft_position(self):
        log_takeoff_queue .info(f"Procurando avião com o número de voo {flight_number} na fila.")
        flight_number= input("Digite o número do voo: ").strip()
        log_takeoff_queue .debug(f"Procurando avião com o número de voo {flight_number} na fila.")
        for index, aircraft in enumerate(self.queue):
            if aircraft.flight_number == flight_number:
                log_takeoff_queue .debug(f"Avião com o número de voo {flight_number} encontrado na posição {index + 1}.")
                print(f"O avião com o número de voo {flight_number} está na posição {index + 1} da fila.")
                return index + 1
        print(f"Avião com o número de voo {flight_number} não encontrado na fila.")
        log_takeoff_queue .warning(f"Avião com o número de voo {flight_number} não encontrado na fila.")
        return -1

