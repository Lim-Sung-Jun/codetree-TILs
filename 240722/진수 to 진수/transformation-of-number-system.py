a, b = map(int, input().split())

n = list(map(int, list(input())))

# a 진수 -> 10 진수
num = 0
for i in range(len(n)):
    num = num * a + n[i]

# 10 진수 -> b 진수
result = []
while True:
    if num < b:
        result.append(num % b)
        break
    result.append(num % b)
    num = num // b

for c in result[::-1]:
    print(c, end = '')