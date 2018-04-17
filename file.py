import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

file = open(BASE_PATH + '/_file_test.dat', 'w') # w = escrever
file.write('JAY')
file.write('\n')
file.write('\n')
file.write('\n')
file.write('\n')
file.write('\n')
file.write('JAY2')
file.close()
os.rename(BASE_PATH + '/_file_test.dat', BASE_PATH + '/_file2_test.dat')