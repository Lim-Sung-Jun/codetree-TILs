s_list = input()
count = 0
n = len(s_list)
for i in range(1, n - 2):
    if s_list[i - 1] == '(' and s_list[i] == '(':
        for j in range(i + 1, n):
            if s_list[j - 1] == ')' and s_list[j] == ')':
                count += 1
print(count)