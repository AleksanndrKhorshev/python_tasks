def arithmetic_progression(a1, d, n):
    progression = []

    for i in range(n):
        an = a1 + i * d
        progression.append(an)

    return progression

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

result = arithmetic_progression(a1, d, n)

for element in result:
    print(element, end=" ")
