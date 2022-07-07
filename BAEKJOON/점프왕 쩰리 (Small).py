# 16173번 - 점프왕 쩰리 (Small)

## 내 풀이
# - BFS 이용
# - 메모리 : 32440 KB  /  시간 : 88 ms

from collections import deque

def BFS(x,y) :
    q = deque([[x,y]])
    while q :
        x, y = q.popleft()
        t = p[x][y]
        for i in range(2) :
            xx, yy = x+dx[i]*t, y+dy[i]*t
            if xx >= n or yy >= n or xx == x and yy == y: continue
            if p[xx][yy] == p[n-1][n-1]  : return 'HaruHaru'
            q.append([xx,yy])
    return 'Hing'

n = int(input())
p = [ list(map(int, input().rstrip().split())) for _ in range(n) ]
dx,dy = [0,1], [1,0]  # 하(아래)우(오른쪽)
print(BFS(0,0))



## 다른 사람 풀이
# - 메모리 : 29056 KB  /  시간 : 56 ms

n=int(input())
D=[list(map(int,input().split())) for _ in range(n)]
S=[[0]*n for _ in range(n)]  # 새로운 판 하나 더 생성
S[0][0]=1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1 : break
        if i+D[i][j] < n : S[i+D[i][j]][j]+=S[i][j]
        if j+D[i][j] < n : S[i][j+D[i][j]] += S[i][j]
print(['HaruHaru','Hing'][S[n-1][n-1] == 0])
