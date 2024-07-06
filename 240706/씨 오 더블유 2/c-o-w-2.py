# n n_list 
# c o w 순서대로..
# 각각의 위치를 일일이 잡아보며 순서대로 만족해야한다.
# 첫번째 -> 두번째 -> 세번째

n = int(input())
n_list = list(input())

count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if n_list[i] == 'C' and n_list[j] == 'O' and n_list[k] == 'W':
                count += 1

print(count)