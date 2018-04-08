import os


def clear_screen():
    # os.name retorna o sistema operacional que meu programa está rodando
    # nt = windows new tecnology

    # duas formas de fazer um if ternário
    # no python primeiro vc poem o resulta depois poem o if

    # forma 1
    # os.system('cls' if os.name == 'nt' else 'clear')

    # os.name retorna o sistema operacional que meu programa está rodando
    # nt = windows new tecnology
    # forma 2
    os.system('cls') if os.name == 'nt' else os.system('clear')


def hearder_caixa():
    print("****************************************")
    print("* School of Net - Caixa Eletrônico *")
    print("****************************************")


def pause():
    # pausa o programa
    input('pressione <ENTER> para continuar...')