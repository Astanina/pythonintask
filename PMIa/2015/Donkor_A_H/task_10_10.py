﻿#Задача 10. Вариант 10.

#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

#Donkor.A.H.
#27.05.2016
 
print ("""
 			Добро пожаловать в "Игру - Генератор персонажей"
 		Вы можете распределить 30 очков между 4 характеристиками:
 	Сила, здоровье, Мудрость и Ловкость. Так же вы можете брать очки, как из общего числа пунктов, так и возвращать эти очки обратно. Удачи!!! И хорошей вам игры!!!
  """)
STR=0
HP=0
INT=0
AGL=0
point=30
number=0
print("Если хотите изменить Силу, то напишите -  Сила. Если Здоровье, то - Здоровье. Если Мудрость, то - Мудрость. Если Ловкость, то - Ловкость")
while True:
       if STR<0 or HP<0 or INT<0 or AGL<0 or point>30:
              print("Ошибка")
              break
              #number=int (inpuit("Напишите слова"))
       elif point==0:
              print("Вы распределили очки. Их распределение:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL)
              break
       print("Ваши очки:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL,"\nНераспределенные очки:",point)
       user_input=input("")
       if user_input=="Сила" :
              number=int(input("Сколько хотите прибавить(отбавить)?"))
              if number <= point :
                            STR=number
                            point-=number
              else :
                     print('Слишком много')
       elif user_input=="Здоровье":
              number=int(input("Сколько хотите прибавить(отбавить)?"))
              if number <= point :
                            HP=number
                            point-=number
              else :
                     print("Слишком много")
       elif user_input=="Мудрость" :
              number=int(input("Сколько хотите прибавить(отбавить)?"))
              if number <= point :
                            INT=number
                            point-=number
              else :
                     print("Слишком много")
       elif user_input=="Ловкость":
              number=int(input("Сколько хотите прибавить(отбавить)?"))
              if number <= point :
                            AGL=number
                            point-=number
              else :
                     print("Слишком много")
inpuit ("\nНажмите ENTER, чтобы завершить")