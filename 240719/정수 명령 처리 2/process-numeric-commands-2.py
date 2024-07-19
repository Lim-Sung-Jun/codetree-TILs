from collections import deque
class q:
    def __init__(self):
        self.queue = deque()

    def push(self, a):
        self.queue.append(a)
    
    def pop(self):
        # if self.empty():
        #     return False
        print(self.queue.popleft())
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if len(self.queue) == 0:
            print(1)
            return True
        else:
            print(0)
            return False
    
    def front(self):
        # if self.empty():
        #     return False
        print(self.queue[0])

n = int(input())
test_q = q()

for i in range(n):
    ins = input().split(' ')
    if len(ins) == 2:
        if ins[0] == 'push':
            test_q.push(ins[1])
    else:
        if ins[0] == 'front':
            test_q.front()
        elif ins[0] == 'size':
            test_q.size()
        elif ins[0] == 'empty':
            test_q.empty()
        elif ins[0] == 'pop':
            test_q.pop()