# Задача 1. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв"

# text = 'ааб абв аббббв абвв аааб аабв абават'
# text = " ".join(list(filter(lambda x: x.find('абв') == -1,text.split())))
# print(text)

# ------------------------------------------------------------------------

# Задача 2. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# num = input('Введите число: ')
# res = sum(map(int,(filter(lambda x: x != ',' and x != '.', list(num)))))
# print(res)

# ------------------------------------------------------------------------

# Задача 3.  Задайте список из n чисел последовательности (1 + 1/n)^n и 
# выведите на экран их сумму.

# num = int(input('Введите число: '))
# lst = list(map(lambda x: (1+1/x)**x, range(1,num+1)))
# print(lst)
# print('sum =',sum(lst))

# ------------------------------------------------------------------------

# Задача 4. Напишите программу, которая найдет произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй и предпоследний
#  и т.д.

# import math
# from random import randint

# num = int(input('Введите количество элементов случайного списка: '))
# lst = [randint(1,10) for j in range(num)]

# lst1 = [lst[i] for i in range(len(lst)-1, math.floor(len(lst)/2)-1,-1)]
# res = list(map(lambda x,y: x*y, lst, lst1))

# print(lst)
# print(res)

# ----------------------------------------------------------------------------
# Задача 5. Задайте число. Составьте список чисел Фибоначи, в том числе для 
# отрицательных индексов

# num = int(input('Введите число: '))
# lstFib = [0,1]
# list(map(lambda x: lstFib.append(lstFib[x]+lstFib[x+1]), [i for i in range(num)]))
# list(map(lambda x: lstFib.insert(0, lstFib[1]-lstFib[0]), [i for i in range(num)]))
# print(lstFib)
