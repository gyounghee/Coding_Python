# 1697번 - 숨바꼭질

## 내 풀이
# - 메모리 : 32452 KB  /  시간 : 136 ms

#from sys import *
#input = stdin.readline

from collections import deque

s, d = map(int, input().split())
v = [False] * (max(d,s)+2)
t = 0

def find(v, s, d, t):
    v[s] = True
    q = deque([s])
    if s >= d : return s-d
    while q :
        if v[d] == True : return t
        for _ in range(len(q)) :
            n = q.popleft()
            ## ** 순서 주의 **
            if n+1 < len(v) and not v[n+1] : q.append(n+1); v[n+1] = True
            if n-1 >= 0 and not v[n-1] : q.append(n-1); v[n-1] = True
            if n*2 < len(v) and not v[n*2] : q.append(n*2); v[n*2] = True
        t += 1

print(find(v, s, d, t))


## ** 순서 주의 **
# - n=0일때 n*2=0이니 v[0]=True가 됨. 그래서 n=True일때 출력이 정답보다 1크게 나옴
#  → 즉, [ n-1, n+1, n*2 ] 순으로 하면 틀리지만 [ n+1, n-1, n*2 ]는 맞음



## 다른 사람 풀이
# - 메모리 : 29200 KB  /  시간 : 64 ms

def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)
  
import sys
n, k = map(int, sys.stdin.readline().split())
print(find(n, k))
