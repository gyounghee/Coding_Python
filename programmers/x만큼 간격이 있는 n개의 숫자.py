# 함수 solution은 정수 x와 자연수 n을 입력 받아
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴

# ** 제한 조건 **
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.

def solution(x, n):
    answer = [x]
    for i in range(n-1):
        answer.append(answer[-1] + x)
    return answer

# TEST CASE Ⅰ
x, n = 2, 5
print(solution(x,n))   # [2,4,6,8,10]

# TEST CASE Ⅱ
x, n = 4, 3
print(solution(x,n))   # [4,8,12]

# TEST CASE Ⅲ
x, n = -4, 2
print(solution(x,n))   # [-4, -8]
