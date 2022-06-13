# 1978번 - 소수 찾기

from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))

for i in num:
    if i == 1 :
        n -= 1
        continue
    for j in range(2,int(i**(1/2))+1):
        if i % j == 0 :
            n -= 1
            break
print(n)
