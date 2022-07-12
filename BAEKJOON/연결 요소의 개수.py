# 11724번 - 연결 요소의 개수

## 풀이 1
# - DFS 이용
# - 메모리 : 64860 KB  /  시간 : 800 ms

from sys import *
setrecursionlimit(10**6)
input = stdin.readline

def DFS(i) :
    visited[i] = True
    for n in V[i]:
        if not visited[n] : DFS(n)

N, M = map(int, input().split())
V = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    V[i].append(j); V[j].append(i) 

visited = [False]*(N+1)
ans = 0
for i in range(1,N+1):
    if not visited[i] :
        DFS(i)
        ans += 1
        
print(ans)



## 풀이 2
# - BFS 이용
# - 메모리 : 64516 KB  /  시간 : 2640 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(i) :
    q = deque([i])
    while q :
        v = q.popleft()
        visited[v] = True
        for n in V[v]:
            if not visited[n] and n not in q : q.append(n)

N, M = map(int, input().split())
V = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    V[i].append(j); V[j].append(i) 

visited = [False]*(N+1)
ans = 0
for i in range(1,N+1):
    if not visited[i] :
        BFS(i)
        ans += 1
        
print(ans)
