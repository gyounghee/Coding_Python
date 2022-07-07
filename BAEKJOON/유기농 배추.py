# 1012번 - 유기농 배추

## 내 풀이
# - 메모리 : 33220 KB  /  시간 : 84 ms

from sys import *
setrecursionlimit(10**6)   # 1000번보다 많은 재귀가 호출된다면, 필요한 만큼 재귀를 늘려줄 필요 있음
input = stdin.readline

def DFS(xx,yy) :
    if xx >= x or yy >= y or xx < 0 or yy < 0: return 0
    if p[xx][yy] == 1  :
        p[xx][yy] = 0
        DFS(xx-1, yy)  # 상
        DFS(xx+1, yy)  # 하
        DFS(xx, yy-1)  # 좌
        DFS(xx, yy+1)  # 우
        return 1
    return 0

for _ in range(int(input())) :
    x, y, c = map(int, input().split())
    p = [ [0]*y for _ in range(x) ]
    for _ in range(c): 
        r, c = map(int, input().split())
        p[r][c] = 1
    if c == 1 or x*y == c: print(1)   # 배추를 모두 심은 경우 런타임 에러가 난다는 것을 생각지 못함
    else :
        ans = 0
        for i in range(x):
            for j in range(y):
                if DFS(i,j) : ans += 1
        print(ans)




## 풀이 2
# - BFS 이용
# - 메모리 : 32436 KB  /  시간 : 104 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(r,c) :
    q = deque([[r,c]])
    while q :
        r, c = q.popleft()
        for i in range(4) :
            rx, cy = r+dx[i], c+dy[i]
            if rx >= x or cy >= y or rx < 0 or cy < 0 or p[rx][cy] == 0: continue
            p[rx][cy] = 0
            q.append([rx,cy])
        
dx, dy = [-1,1,0,0], [0,0,-1,1]  # 상하좌우

for _ in range(int(input())) :
    x, y, c = map(int, input().split())
    p = [ [0]*y for _ in range(x) ]
    for _ in range(c): 
        r, c = map(int, input().split())
        p[r][c] = 1
    if c == 1 or x*y == c: print(1)   # 배추를 모두 심은 경우 런타임 에러가 난다는 것을 생각지 못함
    else :
        ans = 0
        for i in range(x):
            for j in range(y):
                if p[i][j] == 1 :
                    BFS(i,j)
                    ans += 1
        print(ans)
