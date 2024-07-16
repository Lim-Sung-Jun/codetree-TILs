# 가로, 세로, 대각선

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input()))

direction = [(-1,0), (-1,1), (0,1), (1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
validation = "LEE"
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            for dx, dy in direction:
                x = i
                y = j
                count = 1
                while True:
                    n_x = x + dx
                    n_y = y + dy
                    if n_x < 0 or n_x >= n or n_y < 0 or n_y >= m:
                        break
                    if validation[count] != graph[n_x][n_y]:
                        break
                    x = n_x
                    y = n_y
                    count += 1
                    if count == 3:
                        answer += 1
                        break
print(answer)