# 11050번 - 이항 계수 1

from functools import reduce

N, K = map(int, input().split())

if K == 0 or N == K :
    print(1)
else : 
    a = list(range(N,N-K,-1))
    b = list(range(1,K+1))
    a, b = reduce(lambda x, y : x*y, a), reduce(lambda x, y : x*y, b)

    print(a//b if b != 0 else 1)



## 다른 사람 풀이
n,k=map(int, input().split())

a, b = 1, 1

while k:
    a*=n
    b*=k
    n-=1
    k-=1
print(a//b)
