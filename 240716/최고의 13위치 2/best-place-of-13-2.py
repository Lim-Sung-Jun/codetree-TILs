# nxn
# 1, 0
# 1*3 격자 2개를 겹치지 않게 적절히 잘 잡아서
# 격자안에 동전의 갯수를 최대로 해라
# ㅇ ㅇ ㅇ 가로 세로가 정해져있어서 쉬웠다.
# 2개를 놓기 위해서 for문을 4번 써야한다. 그나마 줄일 수 있는 방법이 for k in range(i, n):
# graph에 표시를 하려다가 나중에 갯수 세기가 어려울 것 같아서 visited를 만들어서 체크를 했다.
# 둘 수 있는 모든 곳을 둬보고 점수를 구했다.

# 해설지: visited를 사용하지 않고 같은 행인데 열의 차이가 2 이하인 경우는 겹친다고 봄
# # Step2. 두 격자가 겹치는 경우에는 가짓수로 세지 않습니다.
# if i == k and abs(j - l) <= 2:
#         continue

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
        for k in range(i, n):  # 시간 복잡도를 줄이자.
            for x in range(n - 2):
                if visited[k][x] == False and visited[k][x + 1] == False and visited[k][x + 2] == False:
                    count = 0
                    for l in range(3):
                        count += graph[i][j + l]
                        count += graph[k][x + l]
                    answer = max(answer, count)
print(answer)