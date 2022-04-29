# ** 풀이과정 **
# 약수를 구하고
# 24 = [1,2,3,4,6,8,12,24]
# 16 = [1,2,4,8,16]
# 최대 공약수 →  서로 겹치는 약수 중 가장 큰 수 
# 최소 공배수 →  두 수의 곱 / 최대공약수

def solution(n,m):
    answer = []
    n_num ,m_num = [], []
    for i in range(1,n+1):
        if n % i == 0 : n_num.append(i)
    for i in range(1,m+1):
        if m % i == 0 : m_num.append(i)

    for i in range(len(n_num)-1,-1,-1):
        for j in range(len(m_num)-1,-1,-1):
            if n_num[i] == m_num[j] :
                answer.append(m_num[j])
                break
        if len(answer) == 1 : break
    answer.append( n*m//answer[0] )
    return answer 


# TEST CASE Ⅰ
n, m= 3, 12
print(solution(n, m))

# TEST CASE Ⅰ
n, m= 2, 5
print(solution(n, m))



# -----;- ---------------------------
# 다른사람 풀이 Ⅰ
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer


#  다른사람 풀이 Ⅱ
from fractions import gcd   # gcd → 최대 공약수 구하는 함수
def gcdlcm(a, b):
    g = gcd(a,b)
    l = (a*b)//g    # 최소공배수는 두 수의 곱 / 최대공약수 
    return [g,l]
