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