# n개의 숫자 

n = int(input())

n_list = list(map(int, input().split()))

answer = float('-inf')
for i in range(n - 2):
    for j in range(i + 2, n):
        result = n_list[i] + n_list[j]
        answer = max(result, answer)

print(answer)