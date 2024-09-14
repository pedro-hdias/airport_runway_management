def show_menu():
    print("\n===== Sistema de Gerenciamento de Fila de Decolagem =====")
    print("Selecione uma opção:")
    print("1. Adicionar um avião na fila de decolagem")
    print("2. Permitir a decolagem do primeiro avião na fila")
    print("3. Mostrar o total de aviões aguardando na fila de decolagem")
    print("4. Listar todos os aviões na fila de decolagem")
    print("5. Listar as características do próximo a decolar")
    print("6. Mostrar a posição de um avião conforme o número do voo")
    print("0. Sair")

def get_user_option():
    try:
        option = int(input("Digite o número da opção desejada: "))
        if option < 0 or option > 6:
            print("Opção inválida! Por favor, insira um número entre 0 e 6.")
            return -1
        return option
    except ValueError:
        print("Opção inválida! Por favor, insira um número.")
        return -1
