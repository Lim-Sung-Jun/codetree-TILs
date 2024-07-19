n, k = map(int, input().split())

from collections import deque
q = deque()

for i in range(1, n + 1):
    q.append(i)

result = []
while len(q) != 1:
    for i in range(k - 1): # k번째 전까지!
        q.append(q.popleft())
    result.append(q.popleft())
result.append(q[0])
for j in range(len(result)):
    print(result[j], end = ' ')