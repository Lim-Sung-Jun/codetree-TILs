# nxn
# 1, 0
# 1*3 격자 2개를 겹치지 않게 적절히 잘 잡아서
# 격자안에 동전의 갯수를 최대로 해라
# ㅇ ㅇ ㅇ

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = -1
for i in range(n):
    for j in range(n - 2):
        visited = [[False] * n for _ in range(n)]
        visited[i][j] = True
        visited[i][j + 1] = True
        visited[i][j + 2] = True
        for k in range(i, n):
            for x in range(n - 2):
                if visited[k][x] == False and visited[k][x + 1] == False and visited[k][x + 2] == False:
                    count = 0
                    for l in range(3):
                        count += graph[i][j + l]
                        count += graph[k][x + l]
                    answer = max(answer, count)
print(answer)