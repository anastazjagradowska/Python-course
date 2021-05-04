import sys


print('Zadanie 1')

if len(sys.argv) < 2 : print ('Prosze podac parametry: ')
  #sys.exit()
else: 
  my_str = ''.join(sys.argv[1:])
  print(my_str)


print('Zadanie 2')

uppers, lowers, digits, notletters = [], [], [], []

for i in my_str:
  if i.isalpha():
    if i.isupper():
      uppers.append(i)
    else:
      lowers.append(i)
  elif i.isnumeric():
    digits.append(i)
  else:
    notletters.append(i)

print('Uppers:', uppers)
print('Lowers: ', lowers)
print('Digits: ', digits)
print('Notletters: ', notletters)


print('Zadanie 3')

newLowers = []
for i in lowers:
  if i not in newLowers:
    newLowers.append(i)

print(newLowers)
newList = []
newList = [(i, lowers.count(i)) for i in newLowers]
print(newList)


print('Zadanie 4')

newList.sort(key = lambda x: x[1], reverse = True)
print(newList)


print('Zadanie 5')

vowels = ['a', 'e', 'i', 'y', 'o', 'u', 'A', 'E','I', 'Y', 'O', 'U']
vow, cons = 0, 0

for i in lowers:
  if i in vowels:
    vow +=1
for i in uppers:
  if i in vowels:
    vow +=1

print('Vowels', vow)
cons = len(my_str) - vow - len(digits) - len(notletters)
print('Consonants', cons)

newList = [(int(i), vow*int(i)+cons)for i in digits] 
print(newList)