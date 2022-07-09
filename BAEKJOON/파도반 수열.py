# 9461번 - 파도반 수열

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from heapq import *
from sys import *
input = stdin.readline

ans_n = [ int(input()) for _ in int(input()) ]
t = [0,1,1,1,2,2]
for i in range(6,max(ans_n)+1) :
    t.append(t[i-1]+t[i-5])

for i in ans_n:
    print(t[i])



## 다른 사람 풀이

from sys import stdin

P = [0, 1, 1, 1, 2, 2, 3]
for n in range(7, 101):
    P.append(P[n-1] + P[n-5])

next(stdin)
for n in map(int, stdin):
    print(P[n])
