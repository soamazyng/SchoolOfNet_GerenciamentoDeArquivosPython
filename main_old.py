import getpass
import os

account_list = {
    '0001-02': {
        'password': '123456',
        'name': 'fulano da silva',
        'value': 100,
        'admin': False
    },
    '0002-02': {
        'password': '123456',
        'name': 'Cicrano da silva',
        'value': 200,
        'admin': False
    },
    '0003-02': {
        'password': '123456',
        'name': 'Cicrano da silva',
        'value': 200,
        'admin': True
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

while True:

    print("****************************************")
    print("* School of Net - Caixa Eletrônico *")
    print("****************************************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    print(account_typed)
    print(password_typed)

    ## agência, senha, nome, valor

    if account_typed in account_list and password_typed == account_list[account_typed]['password']:

        # os.name retorna o sistema operacional que meu programa está rodando
        # nt = windows new tecnology

        # duas formas de fazer um if ternário
        # no python primeiro vc poem o resulta depois poem o if

        # forma 1
        # os.system('cls' if os.name == 'nt' else 'clear')

        # forma 2
        os.system('cls') if os.name == 'nt' else os.system('clear')

        print("****************************************")
        print("* School of Net - Caixa Eletrônico *")
        print("****************************************")
        print("1 - Saldo")
        print("2 - Saque")

        if account_list[account_typed]['admin']:
            print("10 - Incluir cédulas");

        option_typed = input('Escolha uma das opções acima: ')

        if option_typed == '1':
            # print('Seu saldo é: ' + account_list[account_typed]["value"])
            print('Seu saldo é: %s %s' % (account_list[account_typed]["value"], 'reais'))
        elif option_typed == '10' and account_list[account_typed]['admin']:
            # print('Seu saldo é: ' + account_list[account_typed]["value"])
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')

            # add item ao dictionay
            money_slips[money_bill_typed] += int(amount_typed)

            print(money_slips)

        elif option_typed == '2':

            value_typed = int(input('Digite o valor a ser sacado: '))

            money_slips_user = {}
            value_int = int(value_typed)

            # operador // pega o valor inteiro da divisao
            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print('Caixa sem cédulas para este valor')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]

                print('peque as notas: ')
                print(money_slips_user)


    else:
        print('conta inválida')

    # pausa o programa
    input('pressione <ENTER> para continuar...')

    # os.name retorna o sistema operacional que meu programa está rodando
    # nt = windows new tecnology
    os.system('cls') if os.name == 'nt' else os.system('clear')
