# n개
# 3개 고름 -> carry가 발생x, 숫자 합의 최대
# carry: 수 + 수 > 10의자리
# 각 자릿수를 더해봤을 때 10을 넘으면 안된다.

def Is_carry(a, b, c):
    max_length = max(len(a), len(b))
    max_length = max(max_length, len(c))

    pad_a = max_length - len(a)
    pad_b = max_length - len(b)
    pad_c = max_length - len(c)

    a = [0] * pad_a + a
    b = [0] * pad_b + b
    c = [0] * pad_c + c
    new_list = [0] * max_length
    for i in range(max_length):
        temp = int(a[i]) + int(b[i]) + int(c[i])
        if temp >= 10:
            return True, 0
        else:
            new_list[i] = str(temp)
    # print(new_list)
    return False, int(''.join(new_list)) # 이게 돼야함

n = int(input())

n_list = []

for i in range(n):
    n_list.append(list(str(input())))
# print(n_list)

# [ 5, 2, 2] [6] / -1부터 차례로 더하면서 carry 여부를 확인한다.
# 합의 최댓값

# 문제풀이
# n개 중에서 3개 완전탐색을 위해서 for문을 반복한다.
# carry의 여부를 확인하고, carry가 아니라면 최댓값과 비교한다.
# carry는 각 위치의 합이 10이 넘는지 확인해야하는데 각각의 길이가 다르므로 이를 padding한다.
# max_length를 구하고 max_length에 맞게 패딩
# 패딩 후 각 자리를 확인하면서 10이 넘는지 보고 넘지 않으면 저장한다.
# 리스트에 있는 숫자를 하나의 숫자로 바꾸기 위해서 string을 사용한다.
 
answer = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            flag, value =  Is_carry(n_list[i], n_list[j], n_list[k])
            if not flag:
                answer = max(answer, value)
print(answer)