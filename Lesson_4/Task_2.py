

numb = int(input('Введите натуральное число: '))
i = 2
while numb != 1:
    if numb%i != 0:
        i = i+1
    else:
        numb = numb / i
        print(i)
