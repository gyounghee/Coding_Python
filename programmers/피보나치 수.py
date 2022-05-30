# 피보나치 수

# for문을 이용한 풀이 - 성공
def solution(n):
    f,b = 0,1
    
    if n > 2 :
        for i in range(3,n+1):
            f, b = b, (f+b)
        return (f+b) % 1234567
    else :
        return (f+b) % 1234567


# 재귀를 이용한 풀이   - 실패 (시간초과) or 실패(런타임에러)

# 실패 이유 - 실행하는 터미널 환경에는 '호출 스택'이라는 것이 존재
#           - 재귀 실행 시 호출 스택에 쌓이게 되고 호출 스택의 한계치를 넘어서면 런타임 에러 발생 

def Fibonacci(n):
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    elif n > 1 :
        return Fibonacci(n-1) + Fibonacci(n-2)
    
def solution(n):
    return Fibonacci(n) % 1234567
