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
