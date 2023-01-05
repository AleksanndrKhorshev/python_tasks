#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

number = int(input('Введите размер списка '))
list = []
sum = 0
for i in range(number):
    list_number = int(input(f'Введите число {i+1} '))
    list.append(list_number)
print(list)
list_new = []
for i in list:
    if i not in list_new:
        list_new.append(i)
print(list_new)
