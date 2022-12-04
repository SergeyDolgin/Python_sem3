
# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
# В скобках пример, как это работает!!!



def proizv(spisok):
    a = 1
    r = round((len(spisok)+1)/2)
    print ('Произведение пар чисел списка: [', end= " ")
    for i in range(r):
        a = spisok[i]*spisok[-i-1]
        print(a, end=" ")
    print (']')

print ('Введите количество элементов списка')
n = int(input())
if n<=0:
    print('Вводить нужно было натуральное число')
else:
    from random import randint 
    spisok = [randint(1,10) for x in range(n)]
    print(spisok)
    proizv(spisok)



