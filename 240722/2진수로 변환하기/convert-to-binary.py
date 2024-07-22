n = int(input())

result = []

while True:
    if n < 2:
        break
    result.append(n % 2)
    n = n // 2

result.append(n % 2)

for c in result[::-1]:
    print(c, end = '')