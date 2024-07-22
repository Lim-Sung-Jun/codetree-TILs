# 4, 8

n, b = map(int, input().split())
result = []

while True:
    if n < b:
        result.append(n % b)
        break
    result.append(n % b)
    n = n // b

for c in result[::-1]:
    print(c, end = '')