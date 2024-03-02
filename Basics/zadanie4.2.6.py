a = float(input("Введите коэффициент a"))
b = float(input("Введите коэффициент b"))
c = float(input("Введите коэффициент c"))
D = b ** 2 - 4 * a * c
if D > 0:
    D = D ** 0.5
    x1 = ((-b) + D) / (2 * a)
    x2 = ((-b) - D) / (2 * a)
    y1 = round(x1, 1)
    y2 = round(x2, 1)
    print(y1, y2)
if D == 0:
    x = (-b) / (2 * a)
    y3 = round(x, 1)
    print(y3)
if D < 0:
    print("Корней нет")
