n = int(input())

result = []

while True:
    result.append(n % 2)
    n = n // 2
    if n == 1:
        break

result.append(n % 2)

for c in result[::-1]:
    print(c, end = '')