def solution(a, b):
    for num in range(a, b + 1):
        print(num, end=" ")
    print()
    for dun in range(b, a - 1, -1):
        print(dun)


solution(50, 80)
