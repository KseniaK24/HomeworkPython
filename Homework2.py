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
# list = list()
# k=1
# for i in range(1,number+1):
#     k*=i
#     list.append(k)
# print(list)

# Задача 3.  Задайте список из n чисел последовательности (1 + 1/n)^n и 
# выведите на экран их сумму.

# number = int(input('Введите число n: '))
# list = list()
# sum=0
# for i in range(1,number+1):
#     k= (1+1/i)**i
#     sum+=k
#     list.append(round(k,2))
# print(list)
# print('sum =',round(sum,2))

# Задача 4.  Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции вводятся с клавиатуры .

# import random

# number = int(input('Введите число N: '))
# list = list()
# for i in range(number):
#     k = random.randint(-number,number)
#     list.append(k)
# print(list)

# count = int(input('Введите колличество элементов для подсчета произведения: '))
# result = 1
# for j in range(count):
#     n =int(input('Введите позицию элемента: '))
#     result*= list[n]
# print('Произведение элементов на указанных позициях', result)

# Задача 5. Реализуйте алгоритм перемешивания списка.

# import random

# number = int(input('Введите количесто элементов списка: '))
# list = list()
# for i in range(number):
#     list.append(i)
# print(list)

# for j in range(number):
#     k = random.randint(0,number-1)
#     temp = list[j]
#     list[j]=list[k]
#     list[k]=temp
# print(list)