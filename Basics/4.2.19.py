def solution(a, b, c):
    result = list()
    for num in range(a, b + 1):
        if num % c == 0:
            result.append(num)
    return result
assert solution(50, 90, 5) == [50, 55, 60, 65, 70, 75, 80, 85, 90]
assert solution(-50, -30, 10) == [-50, -40, -30]