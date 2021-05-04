# Zad 1

def pascal(n):  
  triangle = [[0 for x in range(n)] for y in range(n)]

  for line in range(0, n):
    for i in range(0, line + 1):
      if(i == 0 or i == line):
        triangle[line][i] = 1
        print(triangle[line][i], end = ' ')
      else:
        triangle[line][i] = triangle[line - 1][i - 1] + triangle[line - 1][i]
        print(triangle[line][i], end = ' ')
    
    print('\n', end = '')


# Zad 3

def cezar(shift):
  encrypted = []

  with open('tekstPL.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      result = ''
      for i in range(len(line)):
        char = line[i]
        if(char.isupper()):
          result += chr((ord(char) + shift - 65) % 26 + 65)
        elif(char.islower()):
          result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
          result += char

      encrypted.append(result)
    
    with open('tekstPLout.txt', 'w+') as f2:
      for line in encrypted:
        f2.write(line)

# Zad 4

def cezar_decrypt(shift):
  decrypted = []

  with open('tekstPLout.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      result = ''
      for i in range(len(line)):
        char = line[i]
        if(char.isupper()):
          result += chr((ord(char) - shift - 65) % 26 + 65)
        elif(char.islower()):
          result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
          result += char
      
      decrypted.append(result)
    
    with open('tekstPLout_decrypted.txt', 'w+') as f2:
      for line in decrypted:
        f2.write(line)



# Zad 5

def frequency_decrypt():
  polish_frequency = {}
  encrypted_frequency = {}
  with open('czestosci.txt', 'r') as f:

    lines = f.readlines()
    acc = 0
    for line in lines:
      words = line.split()
      polish_frequency[words[0]] = float(words[1])
      acc += float(words[1])

    for key in polish_frequency:
        polish_frequency[key] = polish_frequency[key] / acc

  print(polish_frequency)
      
  lines_decrypted = None  
  with open('tekstPLout.txt', 'r') as f2:

    lines_decrypted = f2.readlines()
    acc = 0 
    for line in lines_decrypted:
      for char in line:
        if(char.islower()):
          if char not in encrypted_frequency:
            encrypted_frequency[char] = 1
          else:
            encrypted_frequency[char] = encrypted_frequency[char] + 1
          acc += 1
        elif(char.isupper()):
          char = char.lower()
          if char not in encrypted_frequency:
            encrypted_frequency[char] = 1
          else:
            encrypted_frequency[char] = encrypted_frequency[char] + 1
          acc += 1

    for key in encrypted_frequency:
      encrypted_frequency[key] = encrypted_frequency[key] / acc

  print(encrypted_frequency)

  decrypted = []
  for line in lines_decrypted:
    result = ''
    for char in line:
      if(char.islower() or char.isupper()):
        char = char.lower()
        dec_frequency = encrypted_frequency[char]

        actual_key = None
        MAX = 1000
        diff = MAX
        for key in polish_frequency:
          if abs(polish_frequency[key] - dec_frequency) < diff:
            actual_key = key
            diff = abs(polish_frequency[key] - dec_frequency)
        
        result += actual_key
      else:
        result += char

    decrypted.append(result)

  with open('5out.txt', 'w+') as f:
    for line in decrypted:
      f.write(line)

        