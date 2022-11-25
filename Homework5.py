# Задача 1. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв"

# text = 'ааб абв аббббв абвв аааб аабв абават'

# text = " ".join(list(filter(lambda x: x.find('абв') == -1,text.split())))

# print(text)
# -------------------------------------------------------------------------

# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?

# import random
# num1= random.randint(1,10)
# num2= random.randint(1,10)
# player1 = input('Введите имя 1 игрока: ')
# player2 = input('Введите имя 2 игрока: ')
# if num1 > num2:
#     m = player1
#     n = player2
# else:
#     m = player2
#     n = player1

# print('На столе 2021 конфета')
# k = 2021
# while True:
#     while True:
#         print('Ход игрока',m,': ')
#         move = int(input())
#         if move <= 28:
#             break
#         print('За один ход можно забрать не более чем 28 конфет')
#     k-= move
#     if k <= 28:
#         print('осталось',k,'конфет')
#         print('Выйграл игрок',n,'!')
#         break
#     temp = m
#     m=n
#     n=temp
#     print('осталось',k,'конфет')

# a) Игра против бота

# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# print('На столе 2021 конфета')
# k = 2021
# if num2 > num1:
#     move = random.randint(1,29)
#     print('Ход бота: ',move)
#     k-= move
#     print('осталось',k,'конфет')
# while True:
#     while True:
#         move = int(input('Ход игрока: '))
#         if move <= 28:
#             break
#         print('За один ход можно забрать не более чем 28 конфет')
#     k-= move
#     if k <= 28:
#         print('осталось',k,'конфет')
#         print('Выйграл бот!')
#         break
#     print('осталось',k,'конфет')
#     move = random.randint(1,29)
#     print('Ход бота: ',move)
#     k-= move
#     if k <= 28:
#         print('осталось',k,'конфет')
#         print('Выйграл игрок!')
#         break
#     print('осталось',k,'конфет')

# b) Бот с "интеллектом"

# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# print('На столе 2021 конфета')
# k = 2021
# if num2 > num1:
#     move = random.randint(1,29)
#     print('Ход бота: ',move)
#     k-= move
#     print('осталось',k,'конфет')
# while True:
#     while True:
#         move = int(input('Ход игрока: '))
#         if move <= 28:
#             break
#         print('За один ход можно забрать не более чем 28 конфет')
#     k-= move
#     if k <= 28:
#         print('осталось',k,'конфет')
#         print('Выйграл бот!')
#         break
#     print('осталось',k,'конфет')
#     if k-29 <= 28:
#         move = k-29
#     else:
#         move = random.randint(1,29)
#     print('Ход бота: ',move)
#     k-= move
#     if k <= 28:
#         print('осталось',k,'конфет')
#         print('Выйграл игрок!')
#         break
#     print('осталось',k,'конфет')

# Задача 3. Создайте программу для игры в "Крестики-нолики"

# dict_field = {
# 'a1': ' ', 'a2': ' ', 'a3': ' ',
# 'b1': ' ', 'b2': ' ', 'b3': ' ',
# 'c1': ' ', 'c2': ' ', 'c3': ' ',
# }

# def Print_field(dict):
#     print('   1     2     3  ','\n',
#     '     |     |     ','\n'
#     'a ',dict['a1'],' | ',dict['a2'],' | ',dict['a3'],'\n'
#     '______|_____|_____','\n'
#     '      |     |     ','\n'
#     'b ',dict['b1'],' | ',dict['b2'],' | ',dict['b3'],'\n'
#     '______|_____|_____','\n'
#     '      |     |     ','\n'
#     'c ',dict['c1'],' | ',dict['c2'],' | ',dict['c3'],'\n'
#     '      |     |     ','\n')

# player1 = input('Введите имя 1 игрока: ')
# player2 = input('Введите имя 2 игрока: ')
# Print_field(dict_field)
# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# if num1 > num2:
#     m = player1
#     n = player2
# else:
#     m = player2
#     n = player1
# k = 'X'
# l = 'O'
# while True:
#     while True:
#         print('Ход игрока',m+',', 'введите букву и цифру поля: ')
#         move = input()
#         move = move.replace(' ', '')
#         if dict_field.get(move, -1) == ' ':
#             break
#         print('Поле занято или не существует, введите еще')
#     dict_field[move] = k
#     if (dict_field['a1'] == dict_field['a2'] == dict_field['a3'] == k or
#     dict_field['b1'] == dict_field['b2'] == dict_field['b3'] == k or
#     dict_field['c1'] == dict_field['c2'] == dict_field['c3'] == k or
#     dict_field['a1'] == dict_field['b1'] == dict_field['c1'] == k or
#     dict_field['a2'] == dict_field['b2'] == dict_field['c2'] == k or
#     dict_field['a3'] == dict_field['b3'] == dict_field['c3'] == k or
#     dict_field['a1'] == dict_field['b2'] == dict_field['c3'] == k or
#     dict_field['a3'] == dict_field['b2'] == dict_field['c1'] == k):
#         Print_field(dict_field)
#         print('Игра окончена. Выйграл игрок', m+'!')
#         break
#     count = 0
#     for i in dict_field.keys():
#         if dict_field[i] != ' ':
#             count+=1
#     if count == 9:
#         Print_field(dict_field)
#         print('Игра окончена. Ничья!') 
#         break
#     temp = k
#     k = l
#     l = temp
#     temp = m
#     m = n
#     n = temp
#     Print_field(dict_field)

# b) Игра с ботом

# dict_field = {
# 'a1': ' ', 'a2': ' ', 'a3': ' ',
# 'b1': ' ', 'b2': ' ', 'b3': ' ',
# 'c1': ' ', 'c2': ' ', 'c3': ' ',
# }

# def Print_field(dict):
#     print('   1     2     3  ','\n',
#     '     |     |     ','\n'
#     'a ',dict['a1'],' | ',dict['a2'],' | ',dict['a3'],'\n'
#     '______|_____|_____','\n'
#     '      |     |     ','\n'
#     'b ',dict['b1'],' | ',dict['b2'],' | ',dict['b3'],'\n'
#     '______|_____|_____','\n'
#     '      |     |     ','\n'
#     'c ',dict['c1'],' | ',dict['c2'],' | ',dict['c3'],'\n'
#     '      |     |     ','\n')

# def Move_bot(dict, k, l):
#     if dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a1'] == k and dict['a2'] == k and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['b1'] == k and dict['b2'] == k and dict['b3'] == ' ':
#         move = 'b3'
#     elif dict['c1'] == k and dict['c2'] == k and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['a2'] == k and dict['a3'] == k and dict['a1'] == ' ':
#         move = 'a1'
#     elif dict['b2'] == k and dict['b3'] == k and dict['b1'] == ' ':
#         move = 'b1'
#     elif dict['c2'] == k and dict['c3'] == k and dict['c1'] == ' ':
#         move = 'c1'
#     elif dict['a1'] == k and dict['b1'] == k and dict['c1'] == ' ':
#         move = 'c1'
#     elif dict['a2'] == k and dict['b2'] == k and dict['c2'] == ' ':
#         move = 'c2'
#     elif dict['a3'] == k and dict['b3'] == k and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['b1'] == k and dict['c1'] == k and dict['a1'] == ' ':
#         move = 'a1'
#     elif dict['b2'] == k and dict['c2'] == k and dict['a2'] == ' ':
#         move = 'a2'
#     elif dict['b3'] == k and dict['c3'] == k and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['a1'] == k and dict['b2'] == k and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['b2'] == k and dict['c3'] == k and dict['a1'] == ' ':
#         move = 'a1'
#     elif dict['b2'] == k and dict['a3'] == k and dict['c1'] == ' ':
#         move = 'c1'
#     elif dict['b2'] == k and dict['c1'] == k and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['a1'] == k and dict['a3'] == k and dict['a2'] == ' ':
#         move = 'a2'
#     elif dict['b1'] == k and dict['b3'] == k and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['c1'] == k and dict['c3'] == k and dict['c2'] == ' ':
#         move = 'c2'
#     elif dict['a1'] == k and dict['c1'] == k and dict['b1'] == ' ':
#         move = 'b1'
#     elif dict['a2'] == k and dict['c2'] == k and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a3'] == k and dict['c3'] == k and dict['b3'] == ' ':
#         move = 'b3'
#     elif dict['a1'] == k and dict['c3'] == k and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a3'] == k and dict['c1'] == k and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a1'] == l and dict['a2'] == l and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['b1'] == l and dict['b2'] == l and dict['b3'] == ' ':
#         move = 'b3'
#     elif dict['c1'] == l and dict['c2'] == l and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['a2'] == l and dict['a3'] == l and dict['a1'] == ' ':
#         move = 'a1'
#     elif dict['b2'] == l and dict['b3'] == l and dict['b1'] == ' ':
#         move = 'b1'
#     elif dict['c2'] == l and dict['c3'] == l and dict['c1'] == ' ':
#         move = 'c1'
#     elif dict['a1'] == l and dict['b1'] == l and dict['c1'] == ' ':
#         move = 'c1'
#     elif dict['a2'] == l and dict['b2'] == l and dict['c2'] == ' ':
#         move = 'c2'
#     elif dict['a3'] == l and dict['b3'] == l and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['b1'] == l and dict['c1'] == l and dict['a1'] == ' ':
#         move = 'a1'
#     elif dict['b2'] == l and dict['c2'] == l and dict['a2'] == ' ':
#         move = 'a2'
#     elif dict['b3'] == l and dict['c3'] == l and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['a1'] == l and dict['b2'] == l and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['b2'] == l and dict['c3'] == l and dict['a1'] == ' ':
#         move = 'a1'
#     elif dict['b2'] == l and dict['a3'] == l and dict['c3'] == ' ':
#         move = 'c3'
#     elif dict['b2'] == l and dict['c1'] == l and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['a1'] == l and dict['a3'] == l and dict['a2'] == ' ':
#         move = 'a2'
#     elif dict['b1'] == l and dict['b3'] == l and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['c1'] == l and dict['c3'] == l and dict['c2'] == ' ':
#         move = 'c2'
#     elif dict['a1'] == l and dict['c1'] == l and dict['b1'] == ' ':
#         move = 'b1'
#     elif dict['a2'] == l and dict['c2'] == l and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a3'] == l and dict['c3'] == l and dict['b3'] == ' ':
#         move = 'b3'
#     elif dict['a1'] == l and dict['c3'] == l and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a3'] == l and dict['c1'] == l and dict['b2'] == ' ':
#         move = 'b2'
#     elif dict['a1'] == ' ' and dict['a2'] == ' ' and dict['a3'] == k:
#         move = 'a1'
#     elif dict['b1'] == ' ' and dict['b2'] == ' ' and dict['b3'] == k:
#         move = 'b1'
#     elif dict['c1'] == ' ' and dict['c2'] == ' ' and dict['c3'] == k:
#         move = 'c1'
#     elif dict['a2'] == ' ' and dict['a3'] == ' ' and dict['a1'] == k:
#         move = 'a3'
#     elif dict['b2'] == ' ' and dict['b3'] == ' ' and dict['b1'] == k:
#         move = 'b3'
#     elif dict['c2'] == ' ' and dict['c3'] == ' ' and dict['c1'] == k:
#         move = 'c3'
#     elif dict['a1'] == ' ' and dict['b1'] == ' ' and dict['c1'] == k:
#         move = 'a1'
#     elif dict['a2'] == ' ' and dict['b2'] == ' ' and dict['c2'] == k:
#         move = 'a2'
#     elif dict['a3'] == ' ' and dict['b3'] == ' ' and dict['c3'] == k:
#         move = 'a3'
#     elif dict['b1'] == ' ' and dict['c1'] == ' ' and dict['a1'] == k:
#         move = 'c1'
#     elif dict['b2'] == ' ' and dict['c2'] == ' ' and dict['a2'] == k:
#         move = 'c2'
#     elif dict['b3'] == ' ' and dict['c3'] == ' ' and dict['a3'] == k:
#         move = 'c3'
#     elif dict['a1'] == ' ' and dict['b2'] == ' ' and dict['c3'] == k:
#         move = 'c1'
#     elif dict['b2'] == ' ' and dict['c3'] == ' ' and dict['a1'] == k:
#         move = 'c3'
#     elif dict['b2'] == ' ' and dict['a3'] == ' ' and dict['c3'] == k:
#         move = 'a3'
#     elif dict['b2'] == ' ' and dict['c1'] == ' ' and dict['a3'] == k:
#         move = 'c1'
#     elif dict['a1'] == ' ' and dict['a3'] == ' ' and dict['a2'] == k:
#         move = 'a1'
#     elif dict['b1'] == ' ' and dict['b3'] == ' ' and dict['b2'] == k:
#         move = 'b1'
#     elif dict['c1'] == ' ' and dict['c3'] == ' ' and dict['c2'] == k:
#         move = 'c1'
#     elif dict['a1'] == ' ' and dict['c1'] == ' ' and dict['b1'] == k:
#         move = 'a1'
#     elif dict['a2'] == ' ' and dict['c2'] == ' ' and dict['b2'] == k:
#         move = 'a2'
#     elif dict['a3'] == ' ' and dict['c3'] == ' ' and dict['b3'] == k:
#         move = 'c3'
#     elif dict['a1'] == ' ' and dict['c3'] == ' ' and dict['b2'] == k:
#         move = 'a1'
#     elif dict['a3'] == ' ' and dict['c1'] == ' ' and dict['b2'] == k:
#         move = 'a3'
#     elif dict['b2'] != ' ' and dict['a3'] == ' ':
#         move = 'a3'
#     elif dict['a1'] == ' ': move  = 'a1'
#     elif dict['a2'] == ' ': move  = 'a2'
#     elif dict['a3'] == ' ': move  = 'a3'
#     elif dict['b1'] == ' ': move  = 'b1'
#     elif dict['b3'] == ' ': move  = 'b3'
#     elif dict['c1'] == ' ': move  = 'c1'
#     elif dict['c2'] == ' ': move  = 'c2'
#     elif dict['c3'] == ' ': move  = 'c3'
#     return move

# k = 'X'
# l = 'O'
# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)

# if num1 > num2:
#     move = Move_bot(dict_field, k, l)
#     dict_field[move] = k
#     temp = k
#     k=l
#     l=temp

# Print_field(dict_field)
# while True:
#     while True:
#         print('Ход игрока, введите букву и цифру поля: ')
#         move = input()
#         move = move.replace(' ', '')
#         if dict_field.get(move, -1) == ' ':
#             break
#         print('Поле занято или не существует, введите еще')
#     dict_field[move] = k
#     if (dict_field['a1'] == dict_field['a2'] == dict_field['a3'] == k or
#     dict_field['b1'] == dict_field['b2'] == dict_field['b3'] == k or
#     dict_field['c1'] == dict_field['c2'] == dict_field['c3'] == k or
#     dict_field['a1'] == dict_field['b1'] == dict_field['c1'] == k or
#     dict_field['a2'] == dict_field['b2'] == dict_field['c2'] == k or
#     dict_field['a3'] == dict_field['b3'] == dict_field['c3'] == k or
#     dict_field['a1'] == dict_field['b2'] == dict_field['c3'] == k or
#     dict_field['a3'] == dict_field['b2'] == dict_field['c1'] == k):
#         Print_field(dict_field)
#         print('Игра окончена. Игрок выйграл!')
#         break
#     count = 0
#     for i in dict_field.keys():
#         if dict_field[i] != ' ':
#             count+=1
#     if count == 9:
#         Print_field(dict_field)
#         print('Игра окончена. Ничья!') 
#         break
#     Print_field(dict_field)
#     temp = k
#     k=l
#     l=temp
#     move = Move_bot(dict_field, k, l)
#     dict_field[move]= k
#     if (dict_field['a1'] == dict_field['a2'] == dict_field['a3'] == k or
#     dict_field['b1'] == dict_field['b2'] == dict_field['b3'] == k or
#     dict_field['c1'] == dict_field['c2'] == dict_field['c3'] == k or
#     dict_field['a1'] == dict_field['b1'] == dict_field['c1'] == k or
#     dict_field['a2'] == dict_field['b2'] == dict_field['c2'] == k or
#     dict_field['a3'] == dict_field['b3'] == dict_field['c3'] == k or
#     dict_field['a1'] == dict_field['b2'] == dict_field['c3'] == k or
#     dict_field['a3'] == dict_field['b2'] == dict_field['c1'] == k):
#         Print_field(dict_field)
#         print('Игра окончена. Бот выйграл!')
#         break
#     count = 0
#     for i in dict_field.keys():
#         if dict_field[i] != ' ':
#             count+=1
#     if count == 9:
#         Print_field(dict_field)
#         print('Игра окончена. Ничья!') 
#         break
#     Print_field(dict_field)
#     temp = k
#     k=l
#     l=temp

# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и
# восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def Compress(data):
#     short_data = ""
#     i = 0
#     while i < len(data):
#         count = 1
#         while i + 1 < len(data) and data[i] == data[i+1]:
#             count += 1
#             i +=1
#         short_data += str(count) + data[i]
#         i += 1
#     return short_data

# def Recovery(data):
#     recov_data = ''
#     count = ''
#     for i in data:
#         if i.isdigit():
#             count += i
#         else:
#             recov_data += i * int(count)
#             count = ''
#     return recov_data

# text = open('text.txt', 'r').readline()
# short_text = Compress(text)
# short_text = open('short_text.txt', 'w').write(short_text)

# recov_text = open('short_text.txt', 'r').readline()
# recov_text = Recovery(recov_text)
# recov_text = open('recov_text.txt', 'w').write(recov_text)
