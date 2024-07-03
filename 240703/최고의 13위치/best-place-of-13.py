n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = float('-inf')
for i in range(n):
    for j in range(n - 2):
        score = graph[i][j] + graph[i][j + 1] + graph[i][j + 2]
        answer = max(score, answer)
print(answer)