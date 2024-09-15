from controllers.takeoff_queue import TakeoffQueue
from models.aircraft import Aircraft
from views.interface import show_menu, get_user_option
from utils.helpers import configure_logging, validate_input, validate_passengers
import logging, datetime

configure_logging()
log_main = logging.getLogger('main')

takeoff_queue= TakeoffQueue()

def add_flight():
    log_main.info("Adicionando um voo à fila de decolagem.")
    print("\n=== Adicionar Avião ===")
    model= input("Modelo do avião: ").strip()
    airline= input("Empresa aérea: ").strip()
    departure= input("Origem: ").strip()
    arrive= input("Destino: ").strip()
    flight_number= input("Número do voo: ").strip()
    passengers= int(input("Número de passageiros: "))

    if not validate_input(model, airline, departure, arrive, flight_number):
        return  
    if not validate_passengers(passengers):
        return

    try:
        flight= Aircraft(model, airline, departure, arrive, flight_number, passengers)
        log_main.debug(f"Voo criado: {flight}")
        takeoff_queue.add_aircraft(flight)
        log_main.debug("Voo adicionado à fila de decolagem.")
        print("Voo adicionado com sucesso à fila de decolagem.")
    except ValueError as e:
        print(f"Erro ao criar o voo: {e}")
        log_main.error(f"Erro ao criar o voo: {e}")

def takeoff_flight():
    try:
        log_main.info("Decolando um voo.")
        aircraft_taken_off = takeoff_queue.takeoff_aircraft()
        
        if aircraft_taken_off:
            log_main.debug(f"Voo decolado: {aircraft_taken_off}")
            print(f"Voo {aircraft_taken_off.flight_number} decolou com sucesso.")
        else:
            print("Não há voos na fila de decolagem.")
    except ValueError as e:
        log_main.warning(f"Erro ao decolar o voo: {e}")
        print(f"Erro ao decolar o voo: {e}")

def length_takeoff_queue():
    try:
        log_main.info("Obtendo o tamanho da fila de decolagem.")
        total_aircraft= takeoff_queue.get_queue_size()
        print(f"Total de voos na fila de decolagem: {total_aircraft}")
    except ValueError as e:
        log_main.warning(f"Erro ao obter o tamanho da fila de decolagem: {e}")
        print(f"Erro ao obter o tamanho da fila de decolagem: {e}")

def list_all_aircraft():
    try:
        log_main.info("Listando todos os aviões na fila de decolagem.")
        queued_flights = takeoff_queue.list_all_aircraft()
        if queued_flights:
            print("\n=== Voos na Fila de Decolagem ===")
            for idx, flight in enumerate(queued_flights, start=1):
                print(f"{idx}. {flight}")
        else:
            log_main.warning("Fila de decolagem vazia.")
            print("A fila de decolagem está vazia.")
    except ValueError as e:
        log_main.warning(f"Erro ao listar os aviões na fila de decolagem: {e}")
        print(f"Erro ao listar os aviões na fila de decolagem: {e}")

def next_flight_to_takeoff():
    try:
        log_main.info("Obtendo o próximo voo a decolar.")
        next_flight= takeoff_queue.get_next_aircraft()
        if next_flight:
            print(f"\n=== Próximo voo a Decolar ===\n {next_flight}")
        else:
            print("A fila de decolagem está vazia.")
    except ValueError as e: 
        log_main.warning(f"Erro ao obter o próximo voo a decolar: {e}")
        print(f"Erro ao obter o próximo voo a decolar: {e}")

def searching_flight_position():
    try:
        log_main.info("Procurando um voo na fila de decolagem.")
        search_flight_number= input("Digite o número do voo: ").strip()
        position = takeoff_queue.find_aircraft_position(search_flight_number)
        if position != -1:
            print(f"O voo com o número {search_flight_number} está na posição {position} da fila.")
    except ValueError as e:
        log_main.warning(f"Erro ao procurar o voo na fila de decolagem: {e}")
        print(f"Erro ao procurar o voo na fila de decolagem: {e}")

def main():
    while True:
        try:
            log_main.info("Iniciando o programa.")
            show_menu()
            option= get_user_option()
            log_main.debug(f"Opção escolhida: {option}")

            if option == 1:
                add_flight()
            elif option== 2:
                takeoff_flight()
            elif option== 3:
                length_takeoff_queue()
            elif option== 4:
                list_all_aircraft()
            elif option== 5:
                next_flight_to_takeoff()
            elif option== 6:
                searching_flight_position()
            elif option== 0:
                log_main.info("Encerrando o programa.")
                print("Encerrando o programa. Até mais!")
                break
        except Exception as e:
            log_main.error(f"Erro inesperado: {e}")
            print(f"Erro inesperado: {e}")
            break


if __name__ == "__main__":
    main()

