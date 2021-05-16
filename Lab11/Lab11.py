import numpy
import matplotlib.pyplot as plt


print('--Zad1--')

class IFS:
  def __init__(self, v, p):
    self.v = v
    self.p = p
    self.x = [0]
    self.y = [0]

  def transform(self, iter):
    for i in range(iter):
      x = self.x[-1]
      y = self.y[-1]

      nr = numpy.random.choice(numpy.arange(0, len(self.v)), p = self.p)

      v = self.v[nr]

      x_new = v[0] * x + v[1] * y + v[2]
      y_new = v[3] * x + v[4] * y + v[5]

      self.x.append(x_new)
      self.y.append(y_new)

  def draw(self):
    plt.plot(self.x, self.y, '.')
    plt.show()

ifs = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))

ifs.transform(10000)
ifs.draw()


print('--Zad2--')

class Vector:
  def __init__(self, *vec):
    self.tab = []
    for elem in vec:
      self.tab.append(elem)

  def __str__(self):
    return str(self.tab)

  def get_len(self):
    return len(self.tab)

  def __add__(self, vec):
    if type(vec) != Vector and vec.get_len() != self.get_len:
      return 'Wrong vec len or type'
    tab = []
    for i in range(vec.get_len()):
      tab.append(self.tab[i] + vec.tab[i])
    return tab

  def __sub__(self, vec):
    if type(vec) != Vector and vec.get_len() != self.get_len():
      return 'Wrong vec len or type'
    tab = []
    for i in range(vec.get_len()):
      tab.append(self.tab[i] - vec.tab[i])
    return tab

  def __mul__(self, mult):
    tab = []
    for i in range(self.get_len()):
      tab.append(self.tab[i] * mult)
    return tab
  
  def scalar_prod(self, vec):
    if type(vec) != Vector and vec.get_len() != self.get_len:
      return 'Wrong vec len or type'
    acc = 0
    for i in range(self.get_len()):
      acc += self.tab[i] * vec.tab[i]
    return acc

  def vector_prod(self, vec):
    return numpy.cross(self.tab, vec.tab)

  # def mixed_prod(self, vec):

vec1 = Vector(2, 3, 4)
vec2 = Vector(1, 1, 1)
print(vec1)
print(vec1 + vec2)
print(vec1 - vec2)
print(vec1 * 2)
print(vec1.scalar_prod(vec2))
print(vec1.vector_prod(vec2))
print(vec2.vector_prod(vec1))

