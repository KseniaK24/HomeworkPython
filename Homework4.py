# Задача 1. Вычислить число Пи c заданной точностью d.

# d = input('Введите d: ')
# precision = 0
# for i in range(len(d)):
#     if d[i] == ',' or d[i] == '.':
#         precision = len(d)-i-1

# pi = 0
# for i in range(1,100000,4):
#     pi += 4/i - 4/(i+2)

# print(round(pi,precision))
# -----------------------------------------------------------------------

# Задача 2.Задайте натуральное число N. Напишите программу, которая составит
#  список простых множителей числа N. 

# n = int(input('Введите N: '))
# list = []
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)
#         count = 0
#         for j in range(1,i+1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             list.append(i)
# print(list)
# ---------------------------------------------------------------------------

# Задача 3. Задайте последовательность цифр. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

# numbers = input('Введите последовательность цифр: ')
# listInitial = list(numbers)
# listIndex =[]
# for i in range(len(listInitial)):
#     for j in range (i+1, len(listInitial)):
#         if (listInitial[i] == listInitial[j]):
#             listIndex.append(j)
#             listIndex.append(i)
# set = set(listIndex)
# listIndex = list(set)
# listIndex.reverse()
# for k in range(len(listIndex)):
#     listInitial.pop(listIndex[k])
# for k in range(len(listInitial)):
#     listInitial[k] = int(listInitial[k])
# print(listInitial)
# ---------------------------------------------------------------------------

# Задача 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от -100 до 100) многочлена и записать в 
# файл многочлен степени k. k - максимальная степень многочлена, следующий 
# степень следующего на 1 меньше и так до ноля. Коэффициенты расставляет 
# random, поэтому при коэффициенте 0 просто пропускаем данную итерацию 
# степени. Записываем результат в файл.

# k = int(input('Введите к: '))
# text = ''
# import random
# while k > 1:
#     a = random.randint(-100,100)
#     if a != 0:
#         text += str(a) + 'x'+'^'+ str(k)+'+'
#     k-=1
# b = random.randint(-100,100)
# if b != 0:
#     text += str(b) + 'x'+ '+'
# c = random.randint(-100,100)
# if c != 0:
#     text += str(c) + ' = 0'
# text = text.replace('+-', '-')
# text = text.replace('+', ' + ')
# text = text.replace('-', ' - ')
# f = open('task4_1.txt', 'w')
# f.write(text)
# f.close()
# ---------------------------------------------------------------------------

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# def Dict_numbers_polynom(poly):
#     poly = poly.replace(' ', '')
#     dict1 = {}
#     while True:
#         i_degree = poly.find('^')
#         i_plus = poly.find('+',1)
#         i_minus = poly.find('-',1)
#         i_equal = poly.find('=') 
#         a = int(poly[0:i_degree-1])
#         if i_plus != -1 and i_minus != -1: 
#             if i_plus < i_minus:
#                 i_split = i_plus
#             else:
#                 i_split = i_minus
#         if i_plus == -1 and i_minus != -1:
#             i_split = i_minus
#         if i_plus != -1 and i_minus == -1:
#             i_split = i_plus
#         if i_plus == -1 and i_minus == -1:
#             i_split = i_equal
#         degree = int(poly[i_degree+1:i_split])
#         dict1[degree] = a
#         poly = poly[i_split:]
#         if poly.find('^') == -1:
#             break
#     i_x = poly.find('x')
#     if i_x != -1:
#         b = poly[:i_x]
#         if i_x == 1:
#             b = b +'1'
#         dict1[1] = int(b)
#     i_equal = poly.find('=')
#     if i_x != i_equal+1:
#         c = int(poly[i_x+1:i_equal])
#         dict1[0]=c
#     return dict1

# def Max_degree_polynom(poly):
#     poly = poly.replace(' ', '')
#     i_degree = poly.find('^')
#     i_plus = poly.find('+',1)
#     i_minus = poly.find('-',1)
#     i_equal = poly.find('=') 
#     if i_plus != -1 and i_minus != -1: 
#         if i_plus < i_minus:
#             i_split = i_plus
#         else:
#             i_split = i_minus
#     if i_plus == -1 and i_minus != -1:
#         i_split = i_minus
#     if i_plus != -1 and i_minus == -1:
#         i_split = i_plus
#     if i_plus == -1 and i_minus == -1:
#         i_split = i_equal
#     max_degree = poly[i_degree+1:i_split]
#     return int(max_degree)

# f1 = open('task4_1.txt', 'r')
# polynomial1 = f1.readline()

# f2 = open('task4_2.txt', 'r')
# polynomial2 = f2.readline()

# dist_poly1 = Dict_numbers_polynom(polynomial1)
# max_degree1 = Max_degree_polynom(polynomial1)

# dist_poly2 = Dict_numbers_polynom(polynomial2)
# max_degree2 = Max_degree_polynom(polynomial2)

# if max_degree1 < max_degree2:
#     k = max_degree2
# else:
#     k = max_degree1

# text = ''
# while k > 1:
#     a = dist_poly1.get(k,0) + dist_poly2.get(k,0)
#     if a != 0:
#         text += str(a) + 'x'+'^'+ str(k)+'+'
#     k-=1
# b = dist_poly1.get(1,0) + dist_poly2.get(1,0)
# if b != 0:
#     text += str(b) + 'x'+ '+'
# c = dist_poly1.get(0,0) + dist_poly2.get(0,0)
# if c != 0:
#     text += str(c) + ' = 0'
# text = text.replace('+-', '-')
# text = text.replace('+', ' + ')
# text = text.replace('-', ' - ')
# f = open('task5_1.txt', 'w')
# f.write(text)
# f.close()
# f1.close()
# f1.close()