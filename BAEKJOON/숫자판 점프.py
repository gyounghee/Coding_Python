# 2210번 - 숫자판 점프

## 풀이 1
# - 메모리 : 30840 KB  /  시간 : 88 ms

def DFS(x,y,s) :
    if len(s) == 6: ans.add(s)
    for i in range(4) :
        xx, yy = x+dx[i], y+dy[i]
        if xx < 5 and yy < 5 and xx >= 0 and yy >= 0 and len(s) < 6:
            DFS(xx, yy, f'{s}{p[xx][yy]}')

dx, dy = [-1,1,0,0], [0,0,-1,1]
p = [list(input().split()) for _ in range(5)]
ans = set()

for i in range(5) :
    for j in range(5) :
        DFS(i,j, f'{p[i][j]}')

print(len(ans))
