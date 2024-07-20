days_per_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
m1, d1, m2, d2 = map(int, input().split())
key = input()

for i in range(7):
    if days[i] == key:
        key = i # 0
        break

first, second = 0, 0
for i in range(1, m1):
    first += days_per_month[i]
first += d1

for i in range(1, m2):
    second += days_per_month[i]
second += d2

result = abs(second - first) # 1

x = result // 7 # 0
y = result % 7 #

if y >= key:
    x = x + 1

print(x) # 1