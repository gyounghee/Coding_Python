# 2178번 - 미로 탐색

## 내 풀이
# - BFS 이용
# - 메모리 : 32452 KB  /  시간 : 104 ms

from collections import deque
from sys import *
input = stdin.readline

def bfs(r, c) :
    q = deque([[r,c]])
    while q :
        r, c = q.popleft()
        for i in range(4) :
            rx, cy = r+x[i], c+y[i]
            if rx < 0 or rx >= row or cy < 0 or cy >= col :  # 범위를 벗어나면 무시 
                continue 
            if p[rx][cy] == 0 :   # 벽인 경우도 무시
                continue
            if p[rx][cy] == 1 :
                p[rx][cy] = p[r][c]+1
                q.append([rx,cy])
    return p[row-1][col-1]

row, col = map(int, input().split())
p = [ list(map(int, input().rstrip())) for _ in range(row) ]
x,y = [-1,1,0,0], [0,0,-1,1]  # 상하좌우

print(bfs(0,0))
