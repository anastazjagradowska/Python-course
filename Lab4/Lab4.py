import random 
import string 


print('--ZAD 1--')

randomlist = []
print("Podaj liczbe k:")
k = int(input())
for i in range(0, k):
  n = random.randint(0, 5*k)
  randomlist.append(n)
print(randomlist)

firstlist = randomlist.copy()
dictionary = {}
for i in range(100):
  random.shuffle(randomlist)
  shuffle_counter = 0
  for j in range(k):
    if firstlist[j] == randomlist[j]:
      shuffle_counter +=1
  dictionary[i] = shuffle_counter
  print(randomlist)
print(dictionary)

print('--ZAD 2--')

print('Podaj dlugosc k:')
k_1 = int(input())
my_string = ''.join(random.choice(string.ascii_lowercase) for i in range(k_1))
print(my_string)
my_string = my_string.replace('kl', 'k.l')
my_string = my_string.replace('ab', 'a.b')
my_string = my_string.replace('su', 's.u')
my_string = my_string.replace('pe', 'p.e')
my_string = my_string.replace('dd', 'd.e')
print(my_string)


print('--ZAD 3--')

list = [random.randint(0,20) for i in range(100)]
new_dictionary = {}
print(list)

for index, value in enumerate(list):
  ind = [i for i, x in enumerate(list) if x == value]
  new_dictionary.setdefault(value, ind)
print(new_dictionary)


print('--ZAD 4--')

random_list = []
dictionary_palindrom = {}

for i in range(0,1000):
  n = random.randint(100, 999999)
  random_list.append(n)
#print(random_list)

counter = 0
for i in random_list:
  if str(i) == str(i)[::-1]:
    dictionary_palindrom[counter] = i
    counter +=1
print("Otrzymany słownik z liczbami palindromowymi:")
print(dictionary_palindrom)


print('--ZAD 5--')

dictionary1 = {k: random.randint(1, 99) for k in range(0, 10)}
dictionary2 = {k: random.randint(1, 99) for k in range(0, 10)}

print(dictionary1)
print(dictionary2)

dictionary1_copy = {}
dictionary2_copy = {}

for key in dictionary1:
  dictionary1_copy[dictionary1[key]] = key 

for key in dictionary2:
  dictionary2_copy[dictionary2[key]] = key 

print(dictionary1_copy)
print(dictionary2_copy)

dictionary_final = {}
for key in dictionary1_copy:
  if key in dictionary2_copy.keys():
    dictionary_final[key] = (dictionary1_copy[key], dictionary2_copy[key])
print(dictionary_final)