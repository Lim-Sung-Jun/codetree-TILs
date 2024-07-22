binary = list(map(int, list(input())))

# 10진수
num = 0
for i in range(len(binary)):
    num = num * 2 + binary[i]

# 17배
num = num * 17

# 2진수
result = []
while True:
    if num < 2:
        result.append(num % 2)
        break
    result.append(num % 2)
    num = num // 2

for c in result[::-1]:
    print(c, end = '')