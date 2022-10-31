# Задача 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# number = list(input('Введите число: '))
# sum = 0
# for i in range(len(number)):
#     if number[i] != ',' and number[i] != '.':
#         sum+=int(number[i])
# print('Сумма цифр равна', sum)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает
#  набор произведений чисел от 1 до N.

# number = int(input('Введите число: '))
# set = list()
# k=1
# for i in range(1,number+1):
#     k*=i
#     set.append(k)
# print(set)

# Задача 3.  Задайте список из n чисел последовательности (1 + 1/n)^n и 
# выведите на экран их сумму.

# number = int(input('Введите число n: '))
# set = list()
# sum=0
# for i in range(1,number+1):
#     k= (1+1/i)**i
#     sum+=k
#     set.append(round(k,2))
# print(set)
# print('sum =',round(sum,2))

# Задача 4.  Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции вводятся с клавиатуры .

# import random

# number = int(input('Введите число N: '))
# set = list()
# for i in range(number):
#     k = random.randint(-number,number)
#     set.append(k)
# print(set)

# count = int(input('Введите колличество элементов для подсчета произведения: '))
# result = 1
# for j in range(count):
#     n =int(input('Введите позицию элемента: '))
#     result*= set[n]
# print('Произведение элементов на указанных позициях', result)

# Задача 5. Реализуйте алгоритм перемешивания списка.

# import random

# number = int(input('Введите количесто элементов списка: '))
# set = list()
# for i in range(number):
#     set.append(i)
# print(set)

# for j in range(number):
#     k = random.randint(0,number-1)
#     temp = set[j]
#     set[j]=set[k]
#     set[k]=temp
# print(set)