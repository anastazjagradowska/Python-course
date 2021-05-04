print('--Zad 1--')
def print_rows(n, filename, mode):
  with open (filename) as file:
    if mode == 'first':
      print(file.readlines()[:n])

    elif mode == 'last':
      print(file.readlines()[-n:])

    elif mode == 'every_n':
      print(file.readlines()[::10])

    elif mode == 'n_word':
      print(list(map(lambda line: line.split()[n], file.readlines())))

    elif mode == 'n_char':
      print(list(map(lambda line: line[n], file.readlines())))

print('Wypisywanie 20 poczatkowych wierszy pliku:')
print_rows(20, '2020.txt', 'first')

# print('Wypisywanie 20 koncowych wierszy pliku:')
# print_rows(20, '2020.txt', 'last')

# print('Wypisywanie co 10 slowa ze wszystkich wierszy:')
# print_rows(10, '2020.txt', 'every_n')

# print('Wypisywanie pierwszego slowa ze wszyskich wierszy:')
# print_rows(0, '2020.txt', 'n_word')
# print('Wypisywanie drugiego slowa ze wszyskich wierszy:')
# print_rows(1, '2020.txt', 'n_word')

# print('Wypisywanie trzeciego znaku ze wszystkich wierszy:')
# print_rows(2, '2020.txt', 'n_char')


print('--Zad 2--')

import glob
import numpy 

# print(glob.glob('data*.in'))

files_descriptions = []
for file in glob.glob('data*.in'):
  files_descriptions.append(open(file))

all_lines = []
for readfile in files_descriptions:
  all_lines.append(readfile.readlines())

with open('data.out', 'w+') as file:
  for i in range(len(all_lines[0])):
    values_list = []
    for file_lines in all_lines:
      values_list.append(float(file_lines[i]))

    # print(values_list)

    avg_val = numpy.average(values_list)
    std_val = numpy.std(values_list)

    line_to_write = str(i+1) + ' ' + str(avg_val) + ' ' + str(std_val) + '\n'
    file.write(line_to_write)

for file in files_descriptions:
  file.close()


print('--Zad 3--')

def instruction():
  with open('zad3.txt', 'w+') as file:

    line = """import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')

A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z tego skorzystać tylko w skrypcie generującym wykresy)

import numpy
x,y=numpy.loadtxt(nazwa, unpack=True)"""

    file.write(line)

instruction()

