# importa tudo do módulo
# import bank_account_variables

# importa algumas coisas do móculo
from bank_account_variables import account_list, money_slips

import getpass


def show_balance(account_auth):
    # print('Seu saldo é: ' + account_list[account_typed]["value"])
    print('Seu saldo é: %s %s' % (account_list[account_auth]["value"], 'reais'))


def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser incluída: ')

    # add item ao dictionay
    money_slips[money_bill_typed] += int(amount_typed)

    print(money_slips)


def withdraw():
    value_typed = int(input('Digite o valor a ser sacado: '))

    money_slips_user = {}
    value_int = int(value_typed)

    # operador // pega o valor inteiro da divisao
    # if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
    if 0 < value_int // 100 <= money_slips['100']:
        money_slips_user['100'] = value_int // 100
        value_int = value_int - value_int // 100 * 100

    if 0 < value_int // 50 <= money_slips['50']:
        money_slips_user['50'] = value_int // 50
        value_int = value_int - value_int // 50 * 50

    if 0 < value_int // 20 <= money_slips['20']:
        money_slips_user['20'] = value_int // 20
        value_int = value_int - value_int // 20 * 20

    if value_int != 0:
        print('Caixa sem cédulas para este valor')
    else:
        for money_bill in money_slips_user:
            money_slips[money_bill] -= money_slips_user[money_bill]

        print('peque as notas: ')
        print(money_slips_user)


def auth_account():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    print(account_typed)
    print(password_typed)

    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        return account_typed
    else:
        False


def get_menu_options_typed(account_auth):
    print("1 - Saldo")
    print("2 - Saque")

    if account_list[account_auth]['admin']:
        print("10 - Incluir cédulas");

    return input('Escolha uma das opções acima: ')


def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '10' and account_list[account_auth]['admin']:
        insert_money_slips()
    elif option_typed == '2':
        withdraw()
