m1, d1, m2, d2 = map(int, input().split())

days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first, second = 0, 0
for i in range(1, m1):
    first += days_per_month[i]
    # print(days_per_month[i])
first += d1
# print(d1)

for i in range(1, m2):
    second += days_per_month[i]
    # print(days_per_month[i])
second += d2
# print(d2)

print(abs(second - first) + 1)