# 1번 -> 2번 -> .. -> N번
# 체크 포이트 하나 생략 -> 최소 거리
# 또한, 체크 포인트의 좌표는 겹쳐져 주어질 수도 있으며, 이 경우 개발자 A가 체크포인트를 건너뛸 때 그 번호의 체크포인트만 건너뛰게 되며 그 점에 있는 모든 체크포인트를 건너뛰지 않음에 유의합니다.
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

n = int(input())
positions = []
for i in range(n):
    positions.append(list(map(int, input().split())))

# 2번째 ~ n-1번째 건너뜀
# positions[1:-1]에서 -> 순서대로 하나씩 빼먹으면서 거리측정
# 모든 거리를 측정한다.
# 0-1 1-2 2-3 3-4 ... n-2-n-1
# 하나씩 빼면서 거리의 합을 구해준다.
# ㅌ
# 2번
distance_list = []
answer = float('inf')
for i in range(1, n - 1):
    temp = positions.pop(i)
    # print(positions)
    result = 0
    for j in range(n - 2):
        result += distance(positions[j], positions[j + 1])
    answer = min(result, answer)
    positions.insert(i, temp) # insert 중요

print(answer)