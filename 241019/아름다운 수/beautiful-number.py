# 1, 2, 3, 4
# 

n = int(input())

# n -> n자리 모든 수 1,2,3,4를 넣으면서 생기는 케이스
def beauty(n_list):
    i = 0
    while True:
        if i == len(n_list):
            break
        element = n_list[i]
        for j in range(element):
            i = i + j
            if n_list[i] != element:
                return False
        i = i + 1
    return True

def fn(n_list, count):
    # global n
    if n == len(n_list):
        if beauty(n_list):
            return 1

    for i in range(1, n + 1):
        count += fn(n_list + [i], count)
    
    return count

print(fn([], 0))