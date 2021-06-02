import math

print('--Zad1--')

class Point:
  def __init__(self):
    self.x = 0
    self.y = 0

  @property 
  def x(self):
    return self._x

  @x.setter 
  def x(self, x):
    self._x = x

  @x.getter 
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @y.setter 
  def y(self, y):
    self._y = y

  @y.getter
  def y(self):
    return self._y

p = Point()
print(p.x)
print(p.y)

p.x = 4
p.y = 6

print(p.x)
print(p.y)


print('--Zad2--')

def check_limit(first, second):
  def fz(pf):
    def fw(p1, p2):
      if first < p1.x < second and first < p1.y < second and first < p2.x < second and first < p2.y < second:
        return pf(p1, p2)
      else:
        raise Exception
    return fw
  return fz

@check_limit(0, 10)
def add(p1, p2):
  new_p = Point()
  new_p.x = p1.x + p2.x
  new_p.y = p1.y + p2.y
  return new_p

@check_limit(0, 10)
def sub(p1, p2):
  new_p = Point()
  new_p.x = p1.x - p2.x
  new_p.y = p1.y - p2.y
  return new_p

p1_1 = Point()
p1_1.x = 4
p1_1.y = 6

p2_1 = Point()
p2_1.x = 2
p2_1.y = 3

p31_add = add(p1_1, p2_1)
p31_sub = sub(p1_1, p2_1)
print(p31_add.x, p31_add.y)
print(p31_sub.x, p31_sub.y)

p1_2 = Point()
p1_2.x = 11
p1_2.y = 5

p2_2 = Point()
p2_2.x = 2
p2_2.y = 3


print('--Zad3--')

class Geo:
  @staticmethod
  def triangle_perimeter(p1, p2, p3):
    a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) 
    b = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
    c = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)

    return a + b + c

  @staticmethod
  def triangle_area(p1, p2, p3):
    a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) 
    b = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
    c = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
    p = (a + b + c) / 2
    return math.sqrt( p * (p - a) * (p - b) * (p - c))

  @staticmethod
  def quadrangle_perimeter(p1, p2, p3, p4):
    a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) 
    b = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
    c = math.sqrt((p2.x - p4.x) ** 2 + (p2.y - p4.y) ** 2)
    d = math.sqrt((p4.x - p3.x) ** 2 + (p4.y - p3.y) ** 2)
    return a + b + c + d
  
  @staticmethod
  def quadrangle_area(p1, p2, p3, p4):
    a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) 
    b = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
    c = math.sqrt((p2.x - p4.x) ** 2 + (p2.y - p4.y) ** 2)
    d = math.sqrt((p4.x - p3.x) ** 2 + (p4.y - p3.y) ** 2)
    p = (a + b + c + d) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c) * (p - d))

p1 = Point()
p1.x = 2
p1.y = 5

p2 = Point()
p2.x = 11
p2.y = 5

p3 = Point()
p3.x = 4
p3.y = 6

print('Triangle Perimeter ' + str(Geo.triangle_perimeter(p1, p2, p3)))
print('Triange Area ' + str(Geo.triangle_area(p1, p2, p3)))

p4 = Point()
p4.x = 1
p4.y = 1

print('Quadrangle Perimeter ' + str(Geo.quadrangle_perimeter(p1, p2, p3, p4)))
print('Quadrangle Area ' + str(Geo.quadrangle_area(p1, p2, p3, p4)))


print('--Zad4--')

class Dec:
  count_dict = {}
  def __init__(self, pf):
    self.pf = pf
    self.count_dict[pf.__name__] = 0

  def __call__(self, pf):
    Dec.count_dict[self.pf.__name__] += 1
    def fw():
      return self.pf(filter(lambda x: x%2))
    return fw

  @staticmethod
  def get_count():
    print(Dec.count_dict)

@Dec
def fsum(p):
  return sum(p)

@Dec
def fsum2(p):
  return sum(p)

fsum(range(5))
fsum2(range(10))
fsum(range(7))

Dec.get_count()

  