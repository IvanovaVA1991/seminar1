# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
n = float(input("введите число n "))
m = (n%1)*10
if m == 0:
    print("нет")
else:
    print(f"{int(m//1)}")