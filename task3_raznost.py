# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


spisok=[1.1, 1.2, 3.1, 5, 10.01]
drobi=[]
n=0
print('Начальный список', spisok)
for i in spisok:
    if i%1!=0:
        n=round(i%1, 3)
        drobi.append(n)
max_num=max(drobi)
min_num=min(drobi)
print('Максимальная дробная часть', max_num)
print('Минимальная дробная часть',min_num)
result=max_num-min_num
print('Разность', max_num, ' - ', min_num, ' = ',result)