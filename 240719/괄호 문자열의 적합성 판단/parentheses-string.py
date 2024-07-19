s_list = list(input())

stack = []

for i in range(len(s_list)):
    c = s_list[i]
    if c == '(':
        stack.append(c)
    elif c == ')':
        if len(stack) == 0:
            print('No')
            exit()
        stack.pop()
if len(stack) != 0:
    print('No')
    exit()
print('Yes')