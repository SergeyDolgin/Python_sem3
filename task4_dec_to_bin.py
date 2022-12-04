# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number_bin_manual = ''
#     temp = number
#     while temp > 0:
#         number_bin_manual = str(temp % 2) + number_bin_manual
#         temp = temp // 2
#     number_bin_manual ='0b' + number_bin_manual


# print('Введите целое число в десятичной форме')
# num = int(input())

def dec_to_bin (spisok):
    print('Cписок в двоичной системе: [', end=" ")
    for i in range(len(spisok)):
        bin_num = ''
        while spisok[i] > 0:
            bin_num = bin_num + str(spisok[i] % 2)
            spisok[i] = spisok[i] // 2
        print(bin_num,  end=" ")
    print(']')


print('Введите количество элементов списка')
n = int(input())
from random import randint
spisok = [randint(1,100) for x in range(n)]
print('Cписок в десятичной системе:',spisok)
dec_to_bin(spisok)




