# 1009번 - 분산처리

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from sys import *
input = stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    b = b%4 if b%4 != 0 else 4
    print((a**b)%10 if (a**b)%10 != 0 else 10)
