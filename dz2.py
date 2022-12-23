#                        Задача№1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# print('Hello, world!')
# number = float(input('Введите число :'))
# sum = 0.0
# for i in str(number):
#   if i != '.':
#     print(sum)
#     sum = sum + float(i)

# print(sum)

#                        Задача№2
# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.

print('Hello, world!')
n = int(input('Введите нужное количество число :'))
list = []
sum = 0.0
i = 1

for i in range(n):

    if i == 0:
        start = 1
        list.append(round(((1+1/start)**start), 2))
        sum = sum + float((1+1/start)**start)

    else:
        i = i+1
        list.append(round(((1+1/i)**i), 2))
        sum = sum + float((1+1/i)**i)
    
print(f'Для N числа = {n} список:', end=' ')
print(list, sep=', ')
print(f'Сума чисел N = {round(sum, 2)}')


    
        #                        Задача№3
#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

list = [1, 5, 8 , 9 ,10 ]
list2 = []
count = 0
import random
for i in list:

    list2.append(i) 
    num = random.randint(0, (int(len(list)) -1))
    list[count] = list[num]
    list[num] = i
    count= count+1
  
print(f'Перемешанный список:', end=' ')
print(list, sep=', ')
