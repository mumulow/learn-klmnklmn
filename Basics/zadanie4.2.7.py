posl = int(input("введите первое число последовтельности"))
summa = 0
count = 0
if posl == 0:
    print("0, 1")
while posl != 0:
    summa += posl
    count += 1
    posl = int(input("введите следующее число последовательности"))

print("сумма =", summa, "количество =", count)
