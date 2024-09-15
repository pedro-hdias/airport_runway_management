import logging, datetime
from controllers.takeoff_queue import TakeoffQueue

takeoff_queue = TakeoffQueue()

def get_menu():
    menu_display_options = {
        1: "Adicionar um avião na fila de decolagem",
        2: "Permitir a decolagem do primeiro avião na fila",
        3: "Mostrar o total de aviões aguardando na fila de decolagem",
        4: "Listar todos os aviões na fila de decolagem",
        5: "Listar as características do próximo a decolar",
        6: "Mostrar a posição de um avião conforme o número do voo",
        0: "Sair"
    }
    
    function_options = {
        1: takeoff_queue.add_flight,
        2: takeoff_queue.takeoff_flight,
        3: takeoff_queue.get_queue_size,
        4: takeoff_queue.get_list_all_aircraft,
        5: takeoff_queue.get_next_aircraft,
        6: takeoff_queue.get_aircraft_position,
        0: lambda: print("Encerrando o programa. Até mais!")
    }
    return menu_display_options, function_options    

def configure_logging():
    log_file_name = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(
        filename=log_file_name,
        filemode='a',
        format='%(funcName)s - %(levelname)s - %(message)s - %(asctime)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        encoding='utf-8',
        level=logging.DEBUG
    )
