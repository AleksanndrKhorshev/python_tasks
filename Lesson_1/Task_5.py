#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#*Пример:*
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

x1 = float(input("Введите координату X первой точки "))
y1 = float(input("Введите координату Y первой точки "))
x2 = float(input("Введите координату X второй точки "))
y2 = float(input("Введите координату Y второй точки "))
s = float((x2-x1)**2 + (y2-y1)**2)
import math
dist = math.sqrt(s)
print(dist)
