binary = list(input())
binary_int = [int(c) for c in binary]

num = 0

for i in range(len(binary)):
    num = num * 2 + binary_int[i]

print(num)