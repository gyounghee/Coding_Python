# 11286번 - 절대값 힙 

## 내 풀이
# - 메모리 : 34176 KB  /  시간 : 160 ms

from heapq import *
from sys import *
input = stdin.readline

p, m = [], []
heapify(p); heapify(m)

for _ in range(int(input())) :
    n = int(input())
    if n < 0 :
        heappush(m, -n)
    elif n > 0 :
        heappush(p, n)
    else :
        if m : mn = heappop(m)
        else : mn = 0
        if p : pn = heappop(p)
        else : pn = 0
        
        if mn == 0 and pn == 0 : print(0)
        elif mn == 0 and pn != 0 : print(pn)
        elif pn == 0 and mn != 0 : print(-mn)
        elif mn <= pn :
            print(-mn)
            heappush(p, pn)
        else :
            print(pn)
            heappush(m, mn)
