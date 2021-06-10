import mod
import random 


print('--Zad1--')

print(mod.met(1, 2))
print(mod.met(1, 2, 5))
print(mod.met(1, 2, 5, [2, 3, 4]))


print('--Zad3--')

int_dict = {}
range_max = 50
for i in range(range_max):
  int_dict[random.randint(10, 100)] = random.randint(10, 100)
print(int_dict)
print(mod.met3(int_dict))