# 1389번 - 케빈 베이컨의 6단계 법칙 

## 풀이 1
# - 플로이드–워셜 알고리즘
# - 메모리 : 30840 KB  /  시간 : 128 ms

from sys import *
input = stdin.readline

INF = int(1e9)  
N, M = map(int, input().split())
g = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신 초기화
for i in range(N+1) :
    for j in range(N+1) :
        if i == j : g[i][j] = 0

# 관계 입력
for _ in range(M) :
    i, j = map(int, input().split())
    g[i][j] = 1; g[j][i] = 1

# 거리 확인 후 갱신
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1,N+1):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])
t = []
for i in range(1,N+1):
    t.append(sum(g[i][1:]))

print(t.index(min(t))+1)



## 풀이 2
# - BFS 이용
# - 메모리 : 32884 KB  /  시간 : 212 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(i,j,t) :
    q = deque([[i,j,t]])
    while q :
        i, j, t = q.popleft()
        if j in n[i] : return t+1
        else : 
            for k in n[i] :
                q.append([k,j,t+1])


N, M = map(int, input().split())
n = [[] for _ in range(N+1)]

for _ in range(M) :   # 관계 입력
    i, j = map(int, input().split())
    n[i].append(j); n[j].append(i)

ans = [0]*N
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j : continue
        ans[i-1] += BFS(i,j,0)

print(ans.index(min(ans))+1)
