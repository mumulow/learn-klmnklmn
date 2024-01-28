s = str(input('введите строку'))
k = str(input('введите символ вокруг'))
def draw_frame(s, k):
    if not s:
        print("Строка пуста, невозможно нарисовать рамку.")
        return
    print(k * (len(s) + 4))
    print(f"{k} {s} {k}")
    print(k * (len(s) + 4))
