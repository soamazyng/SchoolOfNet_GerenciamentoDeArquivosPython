import os
from bank_account_variables import money_slips

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# #Escreve em um arquivo, dando append 'a' criando um novo sempre 'w'
# # file = open(BASE_PATH + '/_file_test.dat', 'a') # w = escrever
# # file.writelines('JAY')
# # file.write('\n')
# # file.write('\n')
# # file.write('\n')
# # file.write('\n')
# # file.write('\n')
# # file.writelines('JAY2')
# # file.close()
# # os.rename(BASE_PATH + '/_file_test.dat', BASE_PATH + '/_file2_test.dat')
#
# #agora vamos ler o arquivo
#
# file = open(BASE_PATH + '/_file_test.dat', 'r') # w = escrever
# # print(file.read())
# # print(file.read(3)) # tamanho da leitura entre parenteses
#
#
# # lendo linha por linha
# line = file.readline()
#
# while line:
#     print(line)
#     line = file.readline()
#
#
# file.close()


def open_file_bank(mode):
    return open(BASE_PATH + '/' + 'bank_file.dat', mode)


def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill+'='+str(value)+';')


def read_money_splips(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        money_bill_value = line[0:semicolon_pos]
        set_money_bill_value(money_bill_value)
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos + 1:]


def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=')  # 20=5000
    money_bill = money_bill_value[0:equal_pos]
    count_money_bill_value = len(money_bill_value)
    value = money_bill_value[equal_pos + 1:count_money_bill_value]
    print(money_bill, value)
    money_slips[money_bill] = int(value)



def load_bank_data():
    file = open_file_bank('r')
    read_money_splips(file)
