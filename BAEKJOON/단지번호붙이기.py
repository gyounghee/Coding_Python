# 2667번 - 단지번호붙이기

## 풀이 1
# - DFS 이용
# - 메모리 : 31084 KB  /  시간 : 68 ms

from sys import *
input = stdin.readline

def DFS(x,y,t) :
    if x >= N or y >= N or x < 0 or y < 0 or p[x][y] == 0 : return t
    else :
        p[x][y] = 0
        t = t+1
        for i in range(4):
            t = max(t, DFS(x+dx[i], y+dy[i],t))
        return t

dx, dy = [-1,1,0,0], [0,0,-1,1]  

N = int(input())
p = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]
c, ans = 0, []
for i in range(N):
    for j in range(N):
        if p[i][j] == 1 :
            c += 1
            ans.append(DFS(i,j,0))

print(c,'\n'.join(map(str, sorted(ans))),sep='\n')




## 풀이 2
# - BFS 이용
# - 메모리 : 32468 KB  /  시간 : 88 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(x,y) :
    q = deque([[x,y]])
    t = 1
    while q :
        x, y = q.popleft()
        p[x][y] = 0
        for i in range(4) :
            xx, yy = x+dx[i], y+dy[i]
            if xx >= N or yy >= N or xx < 0 or yy < 0 or p[xx][yy] == 0 : continue
            if [xx,yy] not in q :   # 중복확인 방지
                t += 1
                q.append([xx,yy])
    return t

dx, dy = [-1,1,0,0], [0,0,-1,1]  

N = int(input())
p = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]
c, ans = 0, []
for i in range(N):
    for j in range(N):
        if p[i][j] == 1 :
            c += 1
            ans.append(BFS(i,j))

print(c,'\n'.join(map(str, sorted(ans))),sep='\n')
