# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input("введите x "))
y = int(input("введите y "))
if x>0 and y>0:
    print("точка находится в 1 четверти")
if x>0 and y<0:
    print("точка находится в 4 четверти")
if x<0 and y<0:
    print("точка находится в 3 четверти")
if x<0 and y>0:
    print("точка находится во 2 четверти")
