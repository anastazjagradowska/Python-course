import random
import math 
import scipy.misc


print('--Zad 1--')

class Fib_Iter:
  def __init__(self, limit):
    self.first = 0
    self.second = 1
    self.limit = limit

  def __iter__(self):
    return self

  def __next__(self):
    prev = self.first 
    self.first = self.second
    self.second = prev + self.first 
    if prev < self.limit:
      return prev
    raise StopIteration

print('Single Class')
fib = Fib_Iter(10)
for i in fib:
  for j in fib:
    print(f'({i}, {j})', end = ' ')
  print()

print('\n')

for i in Fib_Iter(10):
  for j in Fib_Iter(10):
    print(f'({i}, {j})', end = ' ')
  print()

print('\n')

class Fib_Iter_1:
  def __init__(self, limit):
    self.limit = limit
  
  def __iter__(self):
    return Fib_Iter_2(self.limit)

class Fib_Iter_2:
  def __init__(self, limit):
    self.first = 0
    self.second = 1
    self.limit = limit

  def __next__(self):
    prev = self.first 
    self.first = self.second
    self.second = prev + self.first 
    if prev < self.limit:
      return prev
    raise StopIteration

print('Double Class')
fib = Fib_Iter_1(10)
for i in fib:
  for j in fib:
    print(f'({i}, {j})', end = ' ')
  print()

print('\n')

for i in Fib_Iter_1(10):
  for j in Fib_Iter_1(10):
    print(f'({i}, {j})', end = ' ')
  print()

print('\n')


print('--Zad 2--')

class Random:
  def __init__(self):
    self.m = 2**31 - 1
    self.a = 75
    self.c = 0
    self.x = 1

  def __next__(self):
    self.x = (self.a * self.x + self.c) % self.m
    return self.x/self.m

rand = Random()
limit = 10**5
a_len = [(0.1 * i) for i in range(1, 10)]

def fitSquare(first, second, a_len):
  if abs(first[0] - second[0]) < a_len and abs(first[1] - second[1]) < a_len:
    return 1
  return 0 

a_fit = [0 for i in range (1, 10)]

for i in range(limit):
  first_point = (next(rand), next(rand))
  second_point = (random.random(), random.random())

  for j in range(9):
    a_fit[j] += fitSquare(first_point, second_point, a_len[j])

for i in range(9):
  a_fit[i] /= limit

print(a_fit)


print('--Zad3--')

class NR_iter:
  def __init__(self):
    self.x = 1.5
    self.eps = 10**-5
    self.f = lambda x: math.sin(x) - (0.5 * x) ** 2

  def __iter__(self):
    return self
  
  def __next__(self):
    prev = self.x
    self.x = self.x - (self.f(self.x) / scipy.misc.derivative(self.f, self.x))
    if abs(self.x - prev) < self.eps:
      raise StopIteration
    return prev 

nr_iter = NR_iter()
for i in nr_iter:
  print(i)
    