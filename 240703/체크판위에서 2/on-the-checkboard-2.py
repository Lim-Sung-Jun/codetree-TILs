# 0, 0 -> r - 1, c - 1
# 룰 만족 -> 전체 이동 경로의 수
# 점프: 현재 색 =/= 점프한 곳의 색
# 한칸 이상 오른쪽 or 한칸이상 아래쪽
# 시작 -> 2 곳 -> 도착
# 

r, c = map(int, input().split())

graph = []
for i in range(r):
    graph.append([c for c in input() if c != ' ']) # 공백 지우기
# print(graph)
count = 0

def dfs(n, x, y, value):
    global count
    if n == 3 and x == r - 1 and y == c - 1: # n은 0부터 시작해서 3까지 간다.
        count += 1
        return
    
    for i in range(x + 1, r):
        for j in range(y + 1, c):
            if graph[i][j] != value:
                dfs(n + 1, i, j, graph[i][j])
dfs(0, 0, 0, graph[0][0])

print(count)