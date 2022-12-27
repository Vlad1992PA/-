#                   Задача №1
# 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [2, 3, 5, 9, 3, 5, 8, 9]
sum = 0
count = 0
for i in list:
  if count % 2 != 0:

    sum = sum + i
    count = count+1
  else:
    count = count+1
  
print(f'Сумма чисел нечетных индексов:', sum)

#                   Задача №2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 9, 3, 5, 8, 7]
list_end = []
sum = 0
count = 0
index_min = 0
index_max = -1
while count < len(list)/2:
  #   print(index_min)
  list_end.append(list[index_min] * list[index_max])
  count = count+1
  index_max = index_max - 1
  index_min = index_min + 1

print(f'Произведение пар чисел списка:', end=' ')
print(list_end, sep=', ')

#                   Задача №3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5.1, 10.01]
num = int(list[0])
num2 = list[0]
min = num2 - num
max = num2 - num

for i in list:
    num = int(i)
    num2 = i
    if min > (num2 - num):
        min = num2 - num

for i in list:
    num = int(i)
    num2 = i
    if max < (num2 - num):
        max = num2 - num
print(f'Разница между максимальным и минимальным значением дробной части элементов:',
      round(max - min, 3))


#                   Задача №4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

s = ""
n = int(input(
    "Введите число для преобразовывания десятичного числа в двоичное:"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
    #print(s)
print(s)

#                   Задача №5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
n = int(input('Введите число для перевода:'))
list = [0]
list2 = []
sum = 0
start = 1
variable = 0

for i in range(n-1): # получаем числа фибоначи 
  list.append(sum + start)
  variable = start
  start = sum + start
  sum = variable

sum = 0
start = -1

for i in range(n-1): # получаем числа негафибоначи
  if i % 2 ==0:
    list2.append((sum + start)*-1)
    variable = start
    start = sum + start
    sum = variable
  
  else:
    list2.append(sum + start)
    variable = start
    start = sum + start
    sum = variable

list2.reverse()
print(list2 + list)
