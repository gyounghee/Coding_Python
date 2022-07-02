# 11286번 - 절대값 힙 

## 풀이 1
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



## 풀이 2
# - 메모리 : 34176 KB  /  시간 : 144 ms

from heapq import *
from sys import *
input = stdin.readline

p, m = [], []

for _ in range(int(input())) :
    n = int(input())
    if n < 0 : heappush(m, -n)
    elif n > 0 : heappush(p, n)
    else :
        if p and m :
            if m[0] <= p[0] : print(-heappop(m))
            else : print(heappop(p))
        elif p : print(heappop(p))
        elif m : print(-heappop(m))
        else : print(0)
