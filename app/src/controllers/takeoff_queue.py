from collections import deque
from models.aircraft import Aircraft

class TakeoffQueue:
    """
    Class that manages the aircraft takeoff queue.
    """

    def __init__(self):
        self.queue = deque()

    def add_aircraft(self, aircraft):
        self.queue.append(aircraft)

    def takeoff_aircraft(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return None

    def get_queue_size(self):
        return len(self.queue)

    def list_all_aircraft(self):
        return list(self.queue)

    def get_next_aircraft(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def find_aircraft_position(self, flight_number):
        for index, aircraft in enumerate(self.queue):
            if aircraft.flight_number == flight_number:
                return index + 1
        print(f"Avião com o número de voo {flight_number} não encontrado na fila.")
        return -1
