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



## 다른 사람 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from sys import stdin

n,m = map(int,input().split())

maze = [[0]*(m+2)]
for _ in range(n):
    maze.append([0]+list(map(int,list(stdin.readline().rstrip("\n"))))+[0])
maze.append([0]*(m+2))

que = [(1,1)]
maze[1][1] == 0
count = 1
while True:
    temp = []
    for node in que:
        i,j = node
        if maze[i+1][j] != 0:
            temp.append((i+1,j))
            maze[i+1][j] = 0

        if maze[i-1][j] != 0:
            temp.append((i-1,j))
            maze[i-1][j] = 0

        if maze[i][j+1] != 0:
            temp.append((i,j+1))
            maze[i][j+1] = 0

        if maze[i][j-1] != 0:
            temp.append((i,j-1))
            maze[i][j-1] = 0


    que = temp
    count += 1
    if (n,m) in temp:
        break

print(count)
