# 1,2, ..., k
# n번 반복하여 나올 순서쌍
# k 1, 2, 3
# n 2

k, n = map(int, input().split())

def print_answer(answer):
    for s in answer:
        print(s, end = ' ')
    print()

def f(i, answer):
    if i == n + 1:
        print_answer(answer)
        return
    
    for j in range(1, k + 1):
        answer.append(j)
        f(i + 1, answer)
        answer.pop()
    
f(1, [])