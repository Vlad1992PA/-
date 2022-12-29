import random
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def nameString():
  plenty = {1: '24*x**k + 4*x + 5 = 0',  2: '1*x**k + 5 = 0', 3: '10*x**k = 0'}
  key = random.randint(1, 3)
  string = plenty.get(key)
  return string


formula = nameString()
list = []


def coefficient():
  num = random.randint(-100, 100)
  return num


def stringFormula(string):
  # k = 2 #Используется для решения первого варианта задачи
  count = 0
  for i in string:
    if i.isdigit() and count == 0:
      list.append(coefficient())
      count = count + 1

    elif i.isdigit():
      count = count + 1

    # elif i == 'k': #Используется для решения первого варианта задачи
    #   list.append(k) #Используется для решения первого варианта задачи

    elif i == '=':
      list.append('=')
      list.append(' ')
      list.append('0')
      return list
    else:
      count = 0
      list.append(i)


endFormula = stringFormula(formula)


def printSting(list):
    list2 = []
    k = 2
    for i in list:
        if i == "k":
            list2.append(k)
        else:
            list2.append(i)
    print(f'Задана натуральная степень k = 2', ''.join(map(str, list2)))


printSting(endFormula)


def sumPolynomials(string):
  listInt = []
  num = ''
  count = 1  # счётчик символов + и -
  char = ''

  for i in string:

    if i.isdigit():
      num = num + i

    elif i == '-':
      char = '-'
      count = 1

    elif i == "=":
      return listInt

    else:
      if char == '-' and num.isdigit():
        listInt.append(char + num)
        num = ''
        char = ''
      elif char == '' and num.isdigit():
        listInt.append(num)
        num = ''
      else:
        num


sumPolynomials(''.join(map(str, endFormula)))

sum_list = sumPolynomials(''.join(map(str, endFormula)))


def sumList(list):
  sum = 0
  for i in list:
    sum = sum + int(i)
  return sum


print(f'Cумма многочленов = ', sumList(sum_list))
