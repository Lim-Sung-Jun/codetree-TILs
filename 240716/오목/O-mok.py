# 인덱스 1시작
# 검1/흰2/승부x 0
# 

graph = []
for i in range(19):
    graph.append(list(map(int, input().split())))

# 오른 (x, y + 1)
# 아래 (x + 1, y)
# 오른 아래 대각선 (x + 1, y + 1)
# 5번 이동하고 첫점과 마지막점 검사하기
# 어려웠던점: 6목인지 확인하기 위한 부분은 i - step[0], j - step[1]처럼 일반화할 수 ㅇ ㅣㅆ다
# 빼먹은점: 상하 오른아래대각선 왼아래대각선 모두 고려해야하는데 왼아래대각선은 뺴먹음

flag = True
answer = []
steps = [(0, 1), (1, 0), (1, 1), (1, -1)]
for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            for step in steps:
                x, y = i, j
                count = 1
                flag = True
                while count < 5:
                    n_x = x + step[0]
                    n_y = y + step[1]
                    if 0 <= n_x <= 18 and 0 <= n_y <= 18 and graph[n_x][n_y] == graph[i][j]:
                        x = n_x
                        y = n_y
                    else:
                        flag = False
                        break

                    count += 1

                # 첫 점 끝 점
                if 0 <= i - 1 <= 18 and 0 <= j - 1 <= 18:
                    if graph[i - step[0]][j - step[1]] == graph[i][j]:
                        #print('previous:',i - step[0], j - step[1])
                        flag = False

                if 0 <= x + 1 <= 18 and 0 <= y + 1 <= 18:        
                    if graph[x + step[0]][y + step[1]] == graph[i][j]:
                        #print('next:',x + step[0], y + step[1])
                        flag = False

                if flag == True:
                    answer.append(graph[i][j])
                    answer.append((i + x)/2)
                    answer.append((j + y)/2)
                    #print(answer)
                    break
            if len(answer) != 0:
                break
    if len(answer) != 0:   
        break

if len(answer) != 0:
    print(answer[0])
    print(int(answer[1] + 1), int(answer[2] + 1))
else:
    print(0)