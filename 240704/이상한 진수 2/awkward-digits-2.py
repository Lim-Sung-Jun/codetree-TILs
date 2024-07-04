# 1010 -> 앞에서부터 보고 0있으면 1로 바꾸면 끝
# 1111 -> 전부 1이면 마지막을 0으로 바꾼다
# 0000
n_list = list(input())

flag = False

for i in range(len(n_list)):
    if n_list[i] == '0':
        n_list[i] = '1'
        flag = True
        break

if not flag:
    n_list[-1] = '0'

temp = 1
result = 0
for i in range(len(n_list) - 1, -1, -1):
    result += int(n_list[i]) * temp
    temp = temp * 2
print(result)