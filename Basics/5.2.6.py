import math

numbers = []
x = int(input('введите число для НОК или НОД'))
numbers.append(x)
y = int(input('введите число для НОК или НОД'))
numbers.append(y)
z = int(input('введите число для НОК или НОД'))
numbers.append(z)
lcm = math.lcm(*numbers)
gcd = math.gcd(*numbers)

print("НОК:", lcm)
print("НОД:", gcd)
