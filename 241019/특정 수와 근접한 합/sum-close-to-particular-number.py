n, s = map(int, input().split())
# n-2개를 고르고 합을 구했을 때 s와 가까워지도록 한다.
# abs(합 - s)의 min값 찾기
n_list = list(map(int, input().split()))

# 너무 쉬운 문제였다.
# 해설지에서는 위치를 하나씩 잡아봄
# # # 모든 쌍을 다 잡아봅니다.
# for i in range(n):
#     for j in range(i + 1, n):
#         # i번과 j번 수를 제외할 경우 남은 숫자들의 총합은 다음과 같습니다.
#         new_sum = array_sum - arr[i] - arr[j]
# 일차원일 때 두개를 고르는 모든 쌍은 for문 2개로 구현
# 전체 합에서 두 개 원소 값을 빼주면 된다.
# 와우,,

from itertools import combinations

all_cases = combinations(n_list, len(n_list) - 2)

answer = float('inf')
for cases in all_cases:
    # print(cases)
    temp_sum = sum(cases)
    # print(temp_sum)
    result = abs(s - temp_sum)
    # print(s, temp_sum)
    answer = min(result, answer)
print(answer)