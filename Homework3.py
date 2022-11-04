# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая 
# найдет сумму элементов списка, стоящих на нечетной позиции.

# def ListRandom():
#     listRandom = list()
#     size = int(input('Введите количесто элементов списка: '))
#     valueMin = int(input('Введите минимальное значение списка: '))
#     valueMax = int(input('Введите максимальное значение списка: '))
#     import random
#     for i in range(size):
#         listRandom.append(random.randint(valueMin, valueMax))
#     return listRandom

# def SumOddPositions(list):
#     sum = 0
#     for i in range(1,len(list),2):
#         sum +=list[i]
#     return sum

# listRandom = ListRandom()
# result = SumOddPositions(listRandom)

# print(listRandom)
# print('Cуммa элементов нечетных позиции = ',result)
# ----------------------------------------------------------------

# Задача 2. Напишите программу, которая найдет произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def ListRandom():
#     listRandom = list()
#     size = int(input('Введите количесто элементов списка: '))
#     valueMin = int(input('Введите минимальное значение списка: '))
#     valueMax = int(input('Введите максимальное значение списка: '))
#     import random
#     for i in range(size):
#         listRandom.append(random.randint(valueMin, valueMax))
#     return listRandom

# def ListProductPairs(list1):
#     newList = list()
#     if len(list1) % 2 == 0:
#         lenNewList = len(list1)//2
#     else:
#         lenNewList = len(list1)//2+1
#     for i in range(1,lenNewList+1):
#         newList.append(list1[i-1]*list1[i*(-1)])
#     return newList

# listInitial = ListRandom()
# newList = ListProductPairs(listInitial)

# print(listInitial)
# print(newList)
# -----------------------------------------------------------------

# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдет разницу между максимальным и минимальным значением 
# дробной части элементов.

# def ListRandomReal():
#     listRandomReal = list()
#     size = int(input('Введите количесто элементов списка: '))
#     valueMin = int(input('Введите минимальное значение списка: '))
#     valueMax = int(input('Введите максимальное значение списка: '))
#     import random
#     for i in range(size):
#         listRandomReal.append(round(random.uniform(valueMin, valueMax),2))
#     return listRandomReal

# def ListRemainder(list1):
#     listRemainder = list()
#     for i in range(len(list1)):
#         listRemainder.append(list1[i]%1)
#     return listRemainder

# def FindDifferenceMaxMin(list1):
#     minValue = list1[0]
#     maxValue = list1[0]
#     for i in range(1,len(list1)):
#         if list1[i]< minValue:
#             minValue = list1[i]
#         if list1[i]> maxValue:
#             maxValue = list1[i]
#     return round(maxValue - minValue, 2)

# listRandomReal = ListRandomReal()
# listRemainder = ListRemainder(listRandomReal)
# result = FindDifferenceMaxMin(listRemainder)

# print(listRandomReal)
# print(result)
# -------------------------------------------------------------------------

# Задача 4. Напишите программу, которая будет преобразовывать десятичное
# число в двоичное.

# number = int(input('Введите число: '))
# listBinaryNumber = list()
# i = (-1)
# while number >= 1:
#     if number % 2 == 0:
#         listBinaryNumber.insert(i, 0)
#     else: 
#         listBinaryNumber.insert(i, 1)
#     number //= 2
#     i-=1
# BinaryNumber = ''.join(map(str,listBinaryNumber))

# print(BinaryNumber)
# -----------------------------------------------------------------------

# Задача 5. Задайте число. Составьте список чисел Фибоначи, в том числе для 
# отрицательных индексов

number = int(input('Введите число: '))
listFibonacci = [0,1]
for i in range(number):
    listFibonacci.append(listFibonacci[i] + listFibonacci[i+1])
for i in range(number):
    listFibonacci.insert(0,listFibonacci[1]-listFibonacci[0])
print(listFibonacci)
