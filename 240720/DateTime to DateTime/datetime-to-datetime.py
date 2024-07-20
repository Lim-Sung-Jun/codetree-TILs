days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b, c = map(int, input().split())

second = a * 60 * 24 + b * 60 + c
first = 11 * 60 * 24 + 11 * 60 + 11

result = second - first

if result < 0:
    print(-1)
else:
    print(result)