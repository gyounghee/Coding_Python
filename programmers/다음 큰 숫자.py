# 다음 큰 숫자 

# 실패한 내 답안  - 효율성에서 시간 초과 발생
import re 

def solution(n):
    ori = re.sub(r'[^1]','',bin(n))
    while True :
        n += 1
        if ori == re.sub(r'[^1]','',bin(n)) :
            return n


# 성공한 내 답안  -  효율성 통과 
def solution(n):
    ori = bin(n).replace('0','').replace('b','')
    while True :
        n += 1
        if ori == bin(n).replace('0','').replace('b','') :
            return n



# 다른 사람 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')     # count함수 사용
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n        
