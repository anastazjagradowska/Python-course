import random
import math 
 

print('--Zad 1--')

def gen_natural():
  x = 0
  while 1:
    yield x
    x += 1

def gen_perfect(seq):
  for elem in seq:
    count = 0
    for i in range(1, elem):
      if elem % i == 0:
        count += i

    if count == elem:
      yield elem

def gen_limit(seq, limit):
  for elem in seq:
    if elem < limit:
      yield elem
    else:
      return "Exit"

g = gen_natural()
# g = gen_perfect(range(1000))
# g = gen_limit(range(10000), 100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# for i in gen_limit(gen_perfect(gen_natural()), 10000):
#   print (i)


print('--Zad 2--')

def gen_ui(a):
  u = 0
  x = 1
  while 1:
    if x >= 1.5:
      return 
    u_next = u + a / x
    x_next = x + a
    yield [x_next, u_next, math.log(x_next)]
    x = x_next
    u = u_next

g = gen_ui(0.05)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print('--Zad3--')

def gen_sum(n, i = -1, acc = 0, components = []):
  if i == -1:
    for j in range(1, n):
      yield from gen_sum(n, j, 0, [])
  else:
    if n == acc:
      yield components
    else:
      if acc + i > n:
        for j in range (1, i):
          yield from gen_sum(n, j, acc, components)
      else:
        yield from gen_sum(n, i, acc + i, components + [i])

g = gen_sum(4)
print(next(g))
print(next(g))
print(next(g))


print('--Zad 4--')

def gen_4():
  x =random.random()
  yield x
  while 1:
    y = random.random()
    if y < 0.1:
      return "Wylosowana wartosc jest mneijsza od 0.1"
    elif abs(x - y) > 0.4:
      yield y
      x = y
  
g = gen_4()
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


print('--Zad 5--')

def gen_range(limit1, limit2 = None, step = None):

  if limit2 == None and step == None:
    count = 0.0
    while count < limit1:
      yield count 
      count += 1

  elif step == None:
    count = float(limit1)
    while count < limit2:
      yield count 
      count += 1

  else:
    if limit1 > limit2 and step < 0:
      count = float(limit1)
      while count > limit2:
        yield count 
        count += step 
    elif limit2 > limit1 and step > 0:
      count = float(limit1)
      while count < limit2:
        yield count 
        count += step

print('range(8):', list(gen_range(8)))
print('range(-8):', list(gen_range(-8)))
print('range(1, 8):', list(gen_range(1, 8)))
print('range(8, 1):', list(gen_range(8, 1)))
print('range(1, 8, 2):', list(gen_range(1, 8, 2)))
print('range(1, 8, -2):', list(gen_range(1, 8, -2)))
print('range(8, 1, 2):', list(gen_range(8, 1, 2)))
print('range(8, 1, -2):', list(gen_range(8, 1, -2)))