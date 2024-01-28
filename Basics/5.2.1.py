import math

def sgn(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1

def calculate_expression(x, y):
    result = sgn(x) + y**2 * sgn(y) - abs(x) - math.sqrt(abs(x))
    return result

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

z = calculate_expression(x, y)

print(f"Значение выражения z = {z}")