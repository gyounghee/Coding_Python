# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 한다
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하라

def solution(n):
    if n ** (1/2) == int(n ** (1/2)) :
        return ( n ** (1/2) + 1 ) ** 2
    else :
        return -1


# TEST CASE Ⅰ
n = 121
print(solution(n))  # 144

# TEST CASE Ⅱ
n = 3
print(solution(n))  # -1
