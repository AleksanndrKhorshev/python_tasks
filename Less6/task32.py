import random

def find_indices_in_range(lst, minimum, maximum):
    indices = []

    for i, element in enumerate(lst):
        if minimum <= element <= maximum:
            indices.append(i)

    return indices
random_list = [random.randint(-10, 10) for _ in range(20)]
print("Случайный список:", random_list)

min_val = int(input("Введите минимальное значение диапазона: "))
max_val = int(input("Введите максимальное значение диапазона: "))

result = find_indices_in_range(random_list, min_val, max_val)
print("Индексы элементов, удовлетворяющих диапазону:", result)
