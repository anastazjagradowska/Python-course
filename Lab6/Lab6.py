import time
import sys
import random
from functools import reduce


print('-- Zad 1 --')

powt=1000
N=10000
# DODAWANIE DO LISTY

# def forStatement():
#   my_list = []
#   for i in range(N):
#     my_list.append(i)
#   return my_list

# def listComprehension():
#   return [i for i in range(N)]

# def mapFunction():
#   return map(lambda x: x, range(N))

# def generatorExpression():
#   return (i for i in range(N))

# test dla dodawania do listy:
# [GCC 7.5.0]
# forStatement         => 5607502438
# listComprehension    => 1936492178
# mapFunction          => 2167541
# generatorExpression  => 2238705

# ---------------------------------------------------------------

# DODAWANIE ELEMENTU PODNIESIONEGO DO KWADRATU

# def forStatement():
#   my_list = []
#   for i in range(N):
#     my_list.append(i ** 2)
#   return my_list

# def listComprehension():
#   return [i **2 for i in range(N)]

# def mapFunction():
#   return map(lambda x: x ** 2, range(N))

# def generatorExpression():
#   return (i **2 for i in range(N))

# test dla dodawania elementu podniesionego do kwadratu:
# [GCC 7.5.0]
# forStatement         => 16436497045
# listComprehension    => 13231020147
# mapFunction          => 1801869
# generatorExpression  => 4838251

# ---------------------------------------------------------------

# SUMOWANIE ELEMENTOW Z WYKORZYSTANIEM PETLI FOR 

# def forStatement():
#   my_list = []
#   for i in range(N):
#     my_list.append(i)
#   sum_of_elements = 0
#   for i in my_list:
#     sum_of_elements += i
#   return sum_of_elements

# def listComprehension():
#   my_list = [i for i in range(N)]
#   sum_of_elements = 0
#   for i in my_list:
#     sum_of_elements += i
#   return sum_of_elements

# def mapFunction():
#   my_list = map(lambda x: x, range(N))
#   sum_of_elements = 0
#   for i in my_list:
#     sum_of_elements += i
#   return sum_of_elements


# def generatorExpression():
#   my_list = (i for i in range(N))
#   sum_of_elements = 0
#   for i in my_list:
#     sum_of_elements += i
#   return sum_of_elements

#test dla sumowania elementow z wykorzystaniem petli for:
# [GCC 7.5.0]
# forStatement         => 10257444798
# listComprehension    => 12118691623
# mapFunction          => 8864574052
# generatorExpression  => 7321437696

# ---------------------------------------------------------------

# SUMOWANIE Z WYKORZYSTANIEM FUNCKJI SUM 

# def forStatement():
#   my_list = []
#   for i in range(N):
#     my_list.append(i)
#   sum_of_elements = sum(my_list)
#   return sum_of_elements

# def listComprehension():
#   my_list = [i for i in range(N)]
#   sum_of_elements = sum(my_list)
#   return sum_of_elements

# def mapFunction():
#   my_list = map(lambda x: x, range(N))
#   sum_of_elements = sum(my_list)
#   return sum_of_elements

# def generatorExpression():
#   my_list = (i for i in range(N))
#   sum_of_elements = sum(my_list)
#   return sum_of_elements

#test dla sumowania z wykorzystniem funckji sum:
# [GCC 7.5.0]
# forStatement         => 4630560147
# listComprehension    => 2640515582
# mapFunction          => 4137804335
# generatorExpression  => 5618973680

# ---------------------------------------------------------------

#KONWERSJA OBIEKTU MAP I GENERATORA DO LISTY

def forStatement():
  my_list = []
  for i in range(N):
    my_list.append(i)
  return my_list

def listComprehension():
  return [i for i in range(N)]

def mapFunction():
  return list(map(lambda x: x, range(N)))

def generatorExpression():
  return list((i for i in range(N)))

def tester(testFunction):
  time1 = time.time_ns()
  for i in range(powt):
    testFunction()
  time2 = time.time_ns()
  return time2 - time1

# test dla konwersji obiektu map i generatora do listy:
# [GCC 7.5.0]
# forStatement         => 3199512089
# listComprehension    => 1388752582
# mapFunction          => 3121330211
# generatorExpression  => 2436034604

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))


print('-- Zad 2 --')

N = 20000
distances=[(random.uniform(-1,1)**2 +random.uniform(-1,1)**2)**(1/2) for i in range(N)]
pi = len(list(filter(lambda x: x<=1, distances)))*4/N
print('pi = ', pi)


print('-- Zad 3 --')

N = 20

matrix = []
for i in range(N):
  vector = [random.randint(0, 100) for x in range(N)]
  matrix.append(vector)

# print(matrix)

max_of_row = list(map(lambda x: max(x), matrix))
print('Najwieksza wartosc w kazdym wierszu:', max_of_row)

max_of_column = list(map(lambda x: max(x), zip(*matrix)))
print('Najwieksza wartosc w kazdej kolumnie macierzy', max_of_column)

matrix2 = []
for i in range(N):
  vector = [random.randint(0, 100) for x in range(N)]
  matrix2.append(vector)

# print(matrix2)

matrix3 = []
for i in range(N):
  vector = [random.randint(0, 100) for x in range(N)]
  matrix3.append(vector)

# print(matrix3)

matrixes = [matrix, matrix2, matrix3]
sum_of_matrixes = [list(map(sum, zip(*elements_of_rows))) for elements_of_rows in zip(*matrixes)]
print('Suma dowolnej liczby macierzy:', sum_of_matrixes)


print('-- Zad 4 --')

points = []
for i in range(N):
  points.append([random.randint(0, 100), random.randint(0, 100)])
print('Wspolrzedne punktow na plaszczyznie:', points)

print('Lista, w ktorej pierwszym elementem jest liczba x-ow, a drugim lista y-ow:',reduce(lambda list_x_y, point: [list_x_y[0] + [point[0]], list_x_y[1] + [point[1]]], points, [[], []]))