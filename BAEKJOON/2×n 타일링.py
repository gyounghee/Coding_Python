# 11726번 - 2×n 타일링

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from sys import *
input = stdin.readline

n = int(input())
first, second = 1, 2

if n == 1 : print(1)
elif n == 2 : print(2)
else :
    for _ in range(3,n+1) :
        first, second = second, first+second
    print(second % 10007)
