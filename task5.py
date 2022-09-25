# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("введите x "))
y = int(input("введите y "))
z = int(input("введите z "))
def F(x,y,z):
    F = not(x or y or z)
def P(x,y,z):
    P = not x and not y and not z
if F == P:
    print("утверждение истино")
else:
    print("ложно")
