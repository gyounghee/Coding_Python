# 소수 찾기  (완전탐색)
from itertools import permutations  # 하나의 list에서 조합을 구하기 위한 라이브러리

def solution(numbers):
    n_list = list(numbers)   # numbers에 있는 요소를 쪼개서 list로 저장
    c_num = []
    for i in range(1,len(n_list)+1):
        n_set = set(permutations(n_list,i))
        c_num += list(map(lambda x : int(''.join(x)), n_set))
    c_num = list(set(c_num))   # 조합
    if 0 in c_num : c_num.remove(0)
    if 1 in c_num : c_num.remove(1)

    # 소수 찾기
    PN = len(c_num)
    for n in c_num :
        check, sqrt = 0, int(n ** (1/2))
        for i in range(2,sqrt+1):
            if n % i == 0 :
                PN -= 1
                break
    return PN


# TEST CASE Ⅰ
numbers = "17"
print(solution(numbers))    # 3

# TEST CASE Ⅱ
numbers = "011"
print(solution(numbers))    # 2



## 다른 사람 풀이
from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))  # 조합 만들어서 중복 제거한 후 or연산
    a -= set(range(0, 2))  # set에 0,1 제거 
    for i in range(2, int(max(a) ** 0.5) + 1):  # '에라토스테네스 체' 이용
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
