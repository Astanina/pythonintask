#Задача 4. Вариант 19.
#Напишите программу, которая выводит имя, под которым скрывается Ричард Дженкинс. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Столяров Евгений
# 1.09.2016

name = 'Ричард Дженкинс'
oblast = 'американский актёр кино, театра и телевидения'
birth_place = 'Де-Калб, штат Иллинойс'
birthyear = 1947
age = 2016 - birthyear

print('Имя:', name)
print('Область интересов:', oblast)
print('Год рождения:', birthyear)
print('Возраст:', age)


input("\n\nНажмите Enter для выхода.")