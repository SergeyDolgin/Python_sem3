# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def summa_nechet(spisok):
    r = range (0, n, 2)
    summa = 0
    for i in r:
        summa += spisok[i]
    return summa

print ('Введите количество элементов списка')
n = int(input())
from random import randint 
spisok = [randint(1,10) for x in range(n)]
print(spisok)

x = summa_nechet(spisok)
print('Сумма нечетных элементов списка равна', x)


