# 1, 2, 3, 4
# 

n = int(input())

# n -> n자리 모든 수 1,2,3,4를 넣으면서 생기는 케이스
def beauty(n_list):
    i = 0
    while i < len(n_list):
        # 아래 조건은 while문의 조건으로 넣으면 되징
        # if i >= len(n_list):
        #     break
        element = n_list[i]
        for j in range(element):
            # j를 더하면 0 -> 1 -> 2 -> 3 이렇게 더해지네..
            # 반복한 수를 더해야하니깐 i = i + 1이 맞지 ㅎㅎ 바보양
            # i = i + j
            if i >= len(n_list) or n_list[i] != element:
                return False
            i = i + 1
        # 위에서 i = i + j가 아니라 i = i + 1로 바꿔줬으니 다음 숫자로 넘어갈 필요 x
        # i = i + 1
    return True

def fn(n_list):
    # global n
    if n == len(n_list):
        if beauty(n_list):
            return 1
        # 아닌 경우에도 리턴해야지
        return 0

    # 하나의 트리에서 보면 count는 0이고 자식으로 부터 count를 받는다.
    count = 0
    for i in range(1, 5):
        count += fn(n_list + [i])
    
    return count

print(fn([]))