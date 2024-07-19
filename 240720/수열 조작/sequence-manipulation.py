n = int(input())

from collections import deque
n_list = [i for i in range(1, n + 1)]
q = deque(n_list)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])