n, k = map(int, input().split())

n_list = list(map(int, input().split()))

answer = float('-inf')
for i in range(n - k + 1):
    answer = max(answer, sum(n_list[i : i + k]))

print(answer)