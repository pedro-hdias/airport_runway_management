from controllers.takeoff_queue import TakeoffQueue
from models.aircraft import Aircraft
from views.interface import show_menu, get_user_option
from utils.helpers import validate_input, validate_passengers
import logging
import datetime

log_name_file = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging.basicConfig(
    filename=log_name_file,
    filemode='a',               
    format='%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8',
    level=logging.DEBUG
)

takeoff_queue= TakeoffQueue()

def add_flight():
    logging.info("Adicionando um voo à fila de decolagem.")
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
        logging.info(f"Voo criado: {flight}")
        takeoff_queue.add_aircraft(flight)
        logging.info("Voo adicionado à fila de decolagem.")
        print("Voo adicionado com sucesso à fila de decolagem.")
    except ValueError as e:
        print(f"Erro ao criar o voo: {e}")
        logging.error(f"Erro ao criar o voo: {e}")

def takeoff_flight():
    logging.info("Decolando um voo.")
    aircraft_taken_off = takeoff_queue.takeoff_aircraft()

    if aircraft_taken_off:
        logging.info(f"Voo decolado: {aircraft_taken_off}")
        print(f"Voo {aircraft_taken_off.flight_number} decolou com sucesso.")
    else:
        print("Não há voos na fila de decolagem.")

def lenght_takeoff_queue():
    logging.info("Obtendo o tamanho da fila de decolagem.")
    total_aircraft= takeoff_queue.get_queue_size()
    print(f"Total de voos na fila de decolagem: {total_aircraft}")

def list_all_aircraft():
    logging.info("Listando todos os aviões na fila de decolagem.")
    queued_flights = takeoff_queue.list_all_aircraft()

    if queued_flights:
        print("\n=== Voos na Fila de Decolagem ===")
        for idx, flight in enumerate(queued_flights, start=1):
            print(f"{idx}. {flight}")
    else:
        logging.warning("Fila de decolagem vazia.")
        print("A fila de decolagem está vazia.")

def main():
    logging.info("Iniciando o programa.")

def next_flight_to_takeoff():
    logging.info("Obtendo o próximo voo a decolar.")
    next_flight= takeoff_queue.get_next_aircraft()
    if next_flight:
        print(f"\n=== Próximo voo a Decolar ===\n {next_flight}")
    else:
        print("A fila de decolagem está vazia.")

def searching_flight_position():
    logging.info("Procurando um voo na fila de decolagem.")
    search_flight_number= input("Digite o número do voo: ").strip()
    position = takeoff_queue.find_aircraft_position(search_flight_number)
    if position != -1:
        print(f"O voo com o número {search_flight_number} está na posição {position} da fila.")


def main():
    while True:
        show_menu()
        logging.info("Obtendo a opção do usuário.")
        option= get_user_option()
        logging.debug(f"Opção escolhida: {option}")

        if option == 1:
            add_flight()
        elif option== 2:
            takeoff_flight()
        elif option== 3:
            lenght_takeoff_queue()            
        elif option== 4:
            list_all_aircraft()
        elif option== 5:
            next_flight_to_takeoff()
        elif option== 6:
            searching_flight_position()
        elif option== 0:
            logging.info("Encerrando o programa.")
            print("Encerrando o programa. Até mais!")
            break
        else:
            logging.warning(f"Opção {option} inválida.")
            print("Opção inválida! Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()

