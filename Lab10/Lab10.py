import datetime 


print('--Zad 1--')

def get_add(year):
  if(year >= 1800 and year < 1900):
    return 80
  elif(year >=1900 and year < 2000):
    return 0
  elif(year >= 2000 and year < 2100):
    return 20
  elif(year >= 2100 and year < 2200):
    return 40
  elif(year >= 2200 and year <= 2300):
    return 60

def check_pesel(pesel, date_of_birth, sex):
  try:
    day = date_of_birth.day
    month = date_of_birth.month
    year = date_of_birth.year

    if (int(pesel[0]), int(pesel[1])) != (int(year/10)%10, year%10):
      raise ValueError('Wrong [1-2] numbers')

    pesel_month = month + get_add(year)
    if (int(pesel[2]), int(pesel[3])) != (int(pesel_month/10)%10, pesel_month%10):
      raise ValueError('Wrong [3-4] numbers')

    if(int(pesel[4]), int(pesel[5])) != (int(day/10)%10, day%10):
      raise ValueError('Wrong [5-6] numbers')

    if(int(pesel[9])%2 == 0 and sex == 'man') or (int(pesel[9])%2 == 1 and sex == 'woman'):
      raise ValueError('Wrong [7-10] numbers')

    acc = 0
    mult = 1
    for i in range(10):
      acc += int(pesel[i]) * mult
      mult = (mult + 2)%10 if mult != 3 else 7

    last_result = (10 - (acc%10))%10
    if int(pesel[10]) != last_result:
      raise ValueError('Wrong [11] number')

    print('Pesel %s OK' % pesel)
  except ValueError as err:
    print(err)

check_pesel('02070803628', datetime.datetime(1902, 7, 8), 'woman')
check_pesel('02270803624', datetime.datetime(2002, 7, 8), 'woman')
check_pesel('02270812350', datetime.datetime(2002, 7, 8), 'man')


print('--Zad 2--')

def get_day_ok(day, month, year):
  leap_year = False
  if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
    leap_year = True

  max_day_in_month = None
  if month in [1, 3, 5, 7, 8, 10, 12]:
    max_day_in_month = 31
  elif month in [4, 6, 9, 11]:
    max_day_in_month = 30
  elif leap_year:
    max_day_in_month = 29
  else:
    max_day_in_month = 28
  
  if ( 1<= day <= max_day_in_month):
    return True
  return False

def average_age(restrict = True):
  print('Mode restrict ' + str(restrict))
  with open('daty.in') as f: 
    lines = f.readlines()

    acc = 0
    count = 0
    for line in lines:
      try:
        date_of_birth = line.split()
        day = int(date_of_birth[0])
        month = int(date_of_birth[1])
        year = int(date_of_birth[2])

        if not (1 <= month <= 12):
          print(month)
          raise ValueError('Wrong month')
  
        if not get_day_ok(day, month, year):
          raise ValueError('Wrong day')

        acc += year 
        count += 1
      except:
        if restrict:
          print('Got wrong line - termination')
          return 
        else:
          pass

    avg_age = acc / count 
    print('Average age %s' %str(datetime.datetime.today().year - avg_age))

average_age()
average_age(False)


print('--Zad 3--')

def pythagorean_count(items, four = False):
  items = sorted(items)
  if len(items) == 0:
    raise ValueError('Wrong list lenght')
  
  elems = []
  for i in range(len(items)):
    for j in range(i, len(items)):
      for k in range(j, len(items)):
        if not four:
          if(items[i] ** 2 + items[j] ** 2 == items[k] ** 2):
            elems.append([items[i], items[j], items[k]])
        else:
          for h in range(j, len(items)):
            if(items[i] ** 2 + items[j] ** 2 + items[k] ** 2 == items[h] ** 2):
              elems.append([items[i], items[j], items[k], items[h]])

  if len(elems) == 0:
    raise ValueError('No pythagorean objects')

  print(elems)
  print('Pythagorean count %s'% len(elems))

  objects_moduls = []
  for elem in elems:
    odd = 0
    even = 0
    for item in elem:
      if item % 2 == 0:
        even += 1
      else:
        odd += 1
    objects_moduls.append({
      'odd': odd,
      'even': even,
      'elem': elem
      })

  print('Modulos')
  print(objects_moduls)

pythagorean_count([1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2])
pythagorean_count([1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29])
pythagorean_count([3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17])
pythagorean_count([1,2,3,4,5,6,7,8,9])