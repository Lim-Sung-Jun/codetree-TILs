n = int(input())

# 끝점 무시

# 구간 겹침 x1 -> x2 - 1
offset = 100
n_list = [0 for _ in range(200)]

for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += offset
    x2 += offset

    for j in range(x1, x2):
        n_list[j] += 1

# count = 0
# for i in range(len(n_list)):
#     if n_list[i] > 1:
#         count += 1

print(max(n_list))