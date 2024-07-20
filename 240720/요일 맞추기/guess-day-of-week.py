m1, d1, m2, d2 = map(int, input().split())
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first, second = 0, 0
for i in range(1, m1):
    first += days_per_month[i]
first += d1

for i in range(1, m2):
    second += days_per_month[i]
second += d2

difference = second - first

print(days[difference % 7])