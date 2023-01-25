#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#*Пример:*
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# N = int(input('Введите число '))
#
# fact = 1
# for i in range(N):
#     i = i + 1
#     fact = i * fact
#
#     print(fact, end=" ")


from math import factorial
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x - 1), list(range(1, n+1)))))
