# 2시 5분 -> 1분 -> 60분 시간 분을 0
a, b, c, d = map(int, input().split())

first = a * 60 + b
second = c * 60 + d
print(abs(second - first))