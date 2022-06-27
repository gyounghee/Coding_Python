# 1463번 - 1로 만들기

## 아이디어
# 1. while, for문을 통해 stack에 가능한 계산을 이용하여 계산한 수를 stack에 추가

from sys import *
input = stdin.readline

N = int(input())
ans, stack = 0, [N]

while 1 not in stack :
    tmp = []
    for n in stack :
        if n % 3 == 0 : tmp.append(n//3)
        if n % 2 == 0 : tmp.append(n//2)
        tmp.append(n-1)
    ans += 1
    stack = tmp

print(ans)
