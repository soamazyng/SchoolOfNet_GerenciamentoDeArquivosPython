import os

# pega o caminho absoluto da pasta onde está o arquivo

# abspath('.')--> pega o caminho até chegar neste arquivo
# print(os.path.abspath('.'))

# abspath('.')--> pega o caminho até chegar neste arquivo
path = os.path.abspath('./test/')

# verifica se a pasta existe
# print(os.path.exists(path))

# verifica se é um arquivo
#print(os.path.isfile(path))

# verifica se é uma pasta
# print(os.path.isdir(path))

# retorna o nome do arquivo atual
# print(__file__)

# pega o caminho absoluto sem ter que escrever o nome do arquivo
# print(os.path.abspath(__file__))

# pega a pasta atual do arquivo de forma genérica
print(os.path.dirname(os.path.abspath(__file__)))