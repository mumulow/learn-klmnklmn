sentences = ["Это предложение без цифр", "В этом предложении есть 1 цифра", "55"]

count_with_digit = 0

for sentence in sentences:
    for char in sentence:
        if char.isdigit():
            count_with_digit += 1
            break
print("Количество предложений с цифрой:", count_with_digit)
