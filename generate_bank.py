from utils import hearder_caixa
from file import open_file_bank, write_money_slips

def main():
    hearder_caixa()
    make_money_slips()


def make_money_slips():
    file = open_file_bank()
    write_money_slips(file)
    file.close()


main()
