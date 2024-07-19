from collections import deque

q = deque()

n = int(input())

for i in range(n):
    ins = input().split(' ')

    if len(ins) == 2:
        comm = ins[0]
        val = ins[1]
        if comm == 'push_back':
            q.appendleft(val)
        elif comm == 'push_front':
            q.append(val)
    else:
        comm = ins[0]
        if comm == 'pop_front':
            print(q.pop())
        elif comm == 'front':
            print(q[-1])
        elif comm == 'back':
            print(q[0])
        elif comm == 'size':
            print(len(q))
        elif comm == 'empty':
            if not q:
                print(1)
            else:
                print(0)
        elif comm == 'pop_back':
            print(q.popleft())