n, s = map(int, input().split())
# n-2개를 고르고 합을 구했을 때 s와 가까워지도록 한다.
# abs(합 - s)의 min값 찾기
n_list = list(map(int, input().split()))

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