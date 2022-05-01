# 카펫 - 완전탐
from math import sqrt

def solution(brown, yellow):
    carpet_size = brown+yellow   # 카펫 크기
    sqrt_n = sqrt(carpet_size) # 카펫 크기의 제곱근
    if sqrt_n == int(sqrt_n) :  # 제곱근이 정수라면
        return [ int(sqrt_n), int(sqrt_n) ]   

    h_tmp = int(sqrt_n)
    while True :
        w, h = int( carpet_size/h_tmp ), h_tmp
        if brown == w * 2 + (h - 2) * 2 :
            return [w,h]
        else :
            h_tmp -= 1



# TEST CASE Ⅰ
brown, yellow = 10, 2
print(solution(brown, yellow))   # [4, 3]


# TEST CASE Ⅰ
brown, yellow = 8, 1
print(solution(brown, yellow))   # [3, 3]


# TEST CASE Ⅰ
brown, yellow = 24, 24
print(solution(brown, yellow))   # [8, 6]

# TEST CASE Ⅰ
brown, yellow = 18, 6
print(solution(brown, yellow))   # [8, 3]



## 다른 사람 풀이 - 둘레의 길이 이용
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2*(i + rellow//i) == brown-4:
                return [rellow//i+2, i+2]

