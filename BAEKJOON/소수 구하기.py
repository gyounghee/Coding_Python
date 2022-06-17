# 1929번 - 소수 구하기

N, M = map(int, input().split())

for n in range(N,M+1):
    if n == 1 : continue
    if n == 2 : print(2)
    
    sosu, sqrt = 1, int(n**(1/2))+1
    for i in range(2,sqrt+1):
        if n % i == 0 :
            sosu = 0
            break
    if sosu == 1 :
        print(n)

