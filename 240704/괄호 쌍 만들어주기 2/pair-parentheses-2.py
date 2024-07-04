# 이 문제는 연속이라서 ((를 마주치면 그 앞에 원소들을 전부 돌면서 ))의 갯수를 세준다.
s_list = input()
count = 0
n = len(s_list)
for i in range(1, n - 2):
    if s_list[i - 1] == '(' and s_list[i] == '(':
        for j in range(i + 1, n):
            if s_list[j - 1] == ')' and s_list[j] == ')':
                count += 1
print(count)