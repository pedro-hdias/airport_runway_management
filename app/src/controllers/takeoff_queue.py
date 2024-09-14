from collections import deque
from models.aircraft import Aircraft
import logging

class TakeoffQueue:
    """
    Class that manages the aircraft takeoff queue.
    """

    def __init__(self):
        self.queue = deque()

    def add_aircraft(self, aircraft):
        logging.debug(f"Adicionando avião à fila de decolagem: {aircraft}")
        self.queue.append(aircraft)

    def takeoff_aircraft(self):
        if self.queue:
            logging.debug(f"Decolando o voo: {self.queue[0]}")
            return self.queue.popleft()
        else:
            logging.warning("Fila de decolagem vazia.")
            return None

    def get_queue_size(self):
        logging.debug(f"Tamanho da fila de decolagem: {len(self.queue)}")
        return len(self.queue)

    def list_all_aircraft(self):
        logging.debug(f"Listando todos os aviões na fila de decolagem. {list(self.queue)}")
        if len(self.queue) == 0:
            print("A fila de decolagem está vazia.")
            logging.warning("Tentativa de listar aviões com fila vazia.")
            return []

        return list(self.queue)

    def get_next_aircraft(self):
        if self.queue:
            logging.debug(f"Próximo avião na fila: {self.queue[0]}")
            return self.queue[0]
        else:
            logging.warning("Fila de decolagem vazia.")
            return None

    def find_aircraft_position(self, flight_number):
        logging.debug(f"Procurando avião com o número de voo {flight_number} na fila.")
        for index, aircraft in enumerate(self.queue):
            if aircraft.flight_number == flight_number:
                logging.debug(f"Avião com o número de voo {flight_number} encontrado na posição {index + 1}.")
                return index + 1
        print(f"Avião com o número de voo {flight_number} não encontrado na fila.")
        logging.warning(f"Avião com o número de voo {flight_number} não encontrado na fila.")
        return -1
