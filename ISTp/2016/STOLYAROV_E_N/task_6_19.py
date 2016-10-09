# Задача 6. Вариант 19.
# Создайте игру, в которой компьютер загадывает название одной из шести шахматных фигур, а игрок должен его угадать.

# Столяров Евгений
# 1.09.2016

import random

chess = ['Пешка',
         'Ладья',
         'Конь',
         'Слон',
         'Ферзь',
         'Король']

random_chess = random.choice(chess)
print('Программа случайным образом загадывает название одной из шести шахматных фигур, а игрок должен его угадать.')
print('Допустимые значения: ', end=' ')
for x in chess:
    print(x, end=" ")
print()
my_chess = input('Назовите одну из фигур:')
print()
if my_chess == random_chess:
    print('Вы угадали!')
else:
    print('Вы не угадали =(')
    print('Правильный ответ:', random_chess)

input("\n\nНажмите Enter для выхода.")