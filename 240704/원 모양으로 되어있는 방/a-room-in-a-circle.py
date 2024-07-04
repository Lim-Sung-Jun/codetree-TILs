# # 거리의 최소합? 이해 x

# 어떤 방에서 시작?
# 방에 인원이 들어가는데 거리의 합?
# 2번방 시작
# 예시로 풀었으면 -> n으로 일반화해야지

n = int(input())
room = []

for i in range(n):
    room.append(int(input()))

answer = float('inf')
for i in range(n):
    # visited = [False] * n
    distance = 1
    result = 0
    j = i + 1
    # count = 1 # 이걸 딱 4번만 반목하는 방법? 그냥 for문 쓰면 되는구나 n번 반복이네
    # while count < 5:
    for k in range(n-1):
        result += room[j % n] * distance # 이것도 일반화
        distance += 1
        # count += 1
        j += 1
    answer = min(result, answer)

print(answer)