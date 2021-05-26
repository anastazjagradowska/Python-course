from abc import ABC
from abc import abstractmethod
import numpy
import random

print('--Zad1--')

class Integral(ABC):
  def __init__(self, limit_min, limit_max, steps, func):
    self.limit_min = limit_min
    self.limit_max = limit_max
    self.steps = steps
    self.func = func

    if not (isinstance(self.limit_min, int) and isinstance(self.limit_max, int) and type(self.func) == type(lambda x: x)):
      raise Exception('Wrong params')

  @abstractmethod
  def integrate(self):
    '''Abstract method'''

class Integral_Trapeze(Integral):
  def integrate(self):
    h = (self.limit_max - self.limit_min) / self.steps
    
    acc = 0
    for i in numpy.arange(self.limit_min, self.limit_max, h):
      acc += self.func(i) + self.func(i + 1)

    return (h * acc) / 2

class Integrate_Simpson(Integral):
  def integrate(self):
    h = (self.limit_max - self.limit_min) / (2 * self.steps)

    sum_1 = sum([self.func(self.limit_min + x * h) for x in range(1, (2 * self.steps), 2)])

    sum_2 = sum([self.func(self.limit_min + x * h) for x in range(2, (2 * self.steps) - 2, 2)])

    return h / 3 * (self.func(self.limit_min) + 4 * sum_1 + 2 * sum_2 + self.func(self.limit_max))

limit_min = 2
limit_max = 5
steps = 1000
func = lambda x: x ** 2
Trapeze = Integral_Trapeze(limit_min, limit_max, steps, func)
print('Metoda trapezow: ', Trapeze.integrate())
Simpson = Integrate_Simpson(limit_min, limit_max, steps, func)
print('Metoda Simpsona: ', Simpson.integrate())


print('--Zad2--')

class Stack:
  def __init__(self, stack2 = None):
    if stack2:
      self.stack = [i for i in stack2.stack]
    else:
      self.stack = []

  def push(self, elem):
    self.stack.append(elem)
  
  def pop(self):
    return self.stack.pop(len(self.stack) - 1)

  def push_stack(self, stack2):
    if type(stack2) == Stack or type(stack2) == Sorted_Stack:
      for i in stack2.stack:
        self.push(i)

  def size(self):
    return len(self.stack)

  def __str__(self):
    return str(self.stack)

stack = Stack()
stack.push(2)
stack.push(5)
print(stack.pop())
stack2 = Stack(stack)
stack2.push(10)
stack.push_stack(stack2)
print(stack)

class Sorted_Stack(Stack):
  def __init__(self, stack2 = None):
    if stack2:
      self.stack = [i for i in stack2.stack.sort()]
    else:
      self.stack = []

  def push(self, elem):
    if len(self.stack) == 0:
      self.stack.append(elem)
    elif elem >= self.stack[-1]:
      self.stack.append(elem)

  def push_stack(self, stack2):
    if type(stack2) == Sorted_Stack:
      if len(self.stack) == 0 or stack2.stack[0] >= self.stack[-1]:
        for i in stack2.stack:
          self.push(i)

sorted_stack = Sorted_Stack()
sorted_stack.push(2)
sorted_stack.push(5)
sorted_stack.push(4)
sorted_stack.push_stack(stack2)
print(sorted_stack)
sorted_stack2 = Sorted_Stack()
sorted_stack2.push(11)
sorted_stack2.push(12)
sorted_stack.push_stack(sorted_stack2)
print(sorted_stack)

lens = []
for i in range(100):
  test_stack = Sorted_Stack()
  for i in range(100):
    test_stack.push(random.randint(0, 100))
  lens.append(test_stack.size())

print('Sredni rozmiar posortowanego stosu: ', sum(lens) / len(lens))


print('--Zad3--')

class WC:
  line_count = 0
  word_count = 0
  char_count = 0

  def __init__(self, *files):
    self.files = []
    for file in files:
      self.files.append(file)

  def count (self):
    for file in self.files:
      with open(file, "r") as f:
        line_count = 0
        word_count = 0
        char_count = 0
        for line in f:
          line_count += 1
          word_count += len(line.split())
          char_count += len(line)

        WC.line_count += line_count
        WC.word_count += word_count
        WC.char_count += char_count

        print(line_count, ' ', word_count, ' ', char_count, ' ', file)
    self.count_all()


  @staticmethod
  def count_all():
    print(WC.line_count, ' ', WC.word_count, ' ', WC.char_count, ' ', 'all')

wc = WC('file1.txt', 'file2.txt')
wc.count()