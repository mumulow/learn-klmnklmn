def check_if_head_gets_in_window(a, b, d):
    return a - d >= 2 and b - d >= 2


assert check_if_head_gets_in_window(10, 20, 8) == True
assert check_if_head_gets_in_window(1, 4, 10) == False
print("OK")


def amount_and_sum_of_digits(num):
    digits_count = 0
    digits_sum = 0
    while num > 0:
        digits_sum += num % 10
        digits_count += 1
        num = num // 10
    return digits_count, digits_sum


assert amount_and_sum_of_digits(1) == (1, 1)
assert amount_and_sum_of_digits(1234) == (4, 10)
assert amount_and_sum_of_digits(77777) == (5, 35)
print("OK")


def ski_up(s: float, p: float) -> tuple[list[float], float]:
    """
    1) Заводим пустой список для учета пробегов лыжника за каждый день, начиная со второго
    2) Заводим переменную для подсчета суммы пробегов и ставим ей значение s
    3) 9 раз выполняем следующее:
       3.1) увеличиваем значение переменной s на процент p
       3.2) добавляем s в конец списка
       3.3) увеличиваем значение переменной для подсчета суммы на s
    4) Выводим результат
    """
    assert s > 0
    assert 0 < p <= 100
    uchet_probega = []
    summa = s
    for _ in range(9):
        s = s + s * (p / 100)
        uchet_probega.append(s)
        summa += s
    return uchet_probega, summa


assert ski_up(1, 100) == (sol1 := [2, 4, 8, 16, 32, 64, 128, 256, 512], sum(sol1) + 1)
print("OK")

GLASN = frozenset(["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"])
SOGLASN = frozenset(
    ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
)


def find_glasn_soglasn(sentence: str) -> tuple[int, int]:
    """
    1) Написать списки гласных и согласных букв
    2) Написать цикл с for, проходящий по кажой букве в предложении
    3) Относить каждую букву к гласной или согласной в соответствии с написанными выше списками
    4) Если символ не соответсвует ни одному из списков, то continue
    5) summa_glasn += 1 или summa_sogl += 1
    6) Вывести через return
    """
    summa_glasn = 0
    summa_sogl = 0

    for bukva in sentence:
        bukva = bukva.lower()
        if bukva in GLASN:
            summa_glasn += 1
        elif bukva in SOGLASN:
            summa_sogl += 1
        else:
            continue
    return summa_sogl, summa_glasn


assert find_glasn_soglasn("ы") == (0, 1)
assert find_glasn_soglasn("Привет Андрей") == (8, 4)
assert find_glasn_soglasn("Здравствуй мама я пришел но еще не ОтОшЕл") == (20, 14)
print("OK")


# def what_is_with_lamp():
#   plugged_in = bool(input("Lamp plugged in? "))
#   if not plugged_in:
#     return "Plug in lamp"
#   bulb_burned_out = bool(input("Bulb burned out?"))
#   if not bulb_burned_out:
#     return "Repair lamp"
#   return "Replace Bulb"


from enum import Enum


class Status(str, Enum):
    NEW = "новая"
    ACCEPTED = "принята"


class OrderType(str, Enum):
    COMMON = "обыкновенная"
    LOCATED = "с указанием локации"


order["status"] = Status.NEW
