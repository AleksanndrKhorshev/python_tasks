 #Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#*Пример:*
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите количество чисел в списке: "))
sum = 0
d = {i : 3*i + 1 for i in range(1,number+1)}
print(f"Для n = {number}: {d}")

def sequence(number):
    return[round((1 + 1 / i)**i, 2) for i in range (1, number + 1)]
print(f'Список для {number} чисел =',sequence(number))

for i in range(1, number + 1):
    sum += round((1 + 1 / i) ** i, 2)
print(f'Сумма последовательности из {number} чисел равна: {sum}')