#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
n=int(input('Введите длину списка: '))
a=int(input('Введите минимальное значение списка: '))
b=int(input('Введите максимальное значение списка: '))
numbers = []
for i in range(n):
    numbers.append(randint(a, b))
print(numbers)

min_d=int(input('Введите минимальное значение диапазона: '))
max_d=int(input('Введите максимальное значение диапазона: '))
index=[]
for i in range(len(numbers)):
    if numbers[i]>=min_d and numbers[i]<=max_d:
        ind=i
        index.append(ind)
print(index)