import random


print('Zadanie 1')

def fun1(chain):
  a = random.randint(0, 10)
  b = random.randint(0, 10)
  c = random.randint(0, 10)

  my_list = []

  for i in range(10):
    x = random.uniform(0, 1)
    my_list.append((x, eval(chain)))
  print(my_list)
  return my_list

fun1('a*x+b')


print('Zadanie 2')

def fun2(*d):
  print(d)
  count = len(d)

  dictionary = {}
  for i in d:
    for j in i:
      if j in dictionary:
        dictionary[j] += 1
      else:
        dictionary[j] = 1

  my_list = []
  for key in dictionary:
    if dictionary[key] == count:
      my_list.append(key)

  print(my_list)
  return my_list

fun2([1,2,3], (1,3,5), [3,2])


print('Zadanie 3')
def fun3(a, b, c=True):
  my_list = []
  if c == True:
    my_list = [(a[i], b[i]) for i in range(min(len(a), len(b)))]
  else: 
    my_list = [(a[i] if i < len(a) else None, b[i] if i < len(b) else None) for i in range(max(len(a), len(b)))]
  print(my_list)
  return my_list
fun3([1,2,3,4], [3, 1, 5])
fun3([1,2,3,4], [3, 1, 5], c = False)


