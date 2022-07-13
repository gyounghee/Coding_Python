# 7576번 - 토마토

## 내 풀이 
# - 메모리 : 97988 KB  /  시간 : 2008 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(x,y) :
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < r and yy < c and xx >= 0 and yy >= 0 and t[xx][yy] == 0 :
            t[xx][yy] = 1
            tmp.append((xx,yy))

dx, dy = [-1,1,0,0], [0,0,-1,1]
c, r = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(r)]

n = deque([ (i,j) for i in range(r) for j in range(c) if t[i][j] == 1 ])
ans = -1
while n :
    ans += 1
    tmp = deque([])
    for _ in range(len(n)):
        x, y = n.popleft()
        BFS(x,y)
    n = tmp

for i in range(r):
    if t[i].count(0) :
        ans = -1
        break
print(ans)





## 다른 사람 풀이
# - 메모리 : 71072 KB  /  시간 : 932 ms

from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    N, M = map(int, input().split())  # 행(M)과 열(N) 입력 받음
    length = N * M   # length 변수에 총 길이 저장
    arr = [0] * length    # 총 길이 만큼의 1차원 list 생성
    for i in range(0, length, N):   # 토마토 상태 값을 1차원 list인 arr에 초기화
        arr[i:i+N] = input().split()

    que = deque(i for i in range(length) if arr[i] == '1')  # 값이 1인 인덱스만 que에 저장
    cnt = arr.count('0')  # cnt변수에 0의 개수 저장
    ans = 0

    while cnt and que:  
        ans += 1
        for _ in range(len(que)):
            cur = que.popleft()
            r, c = cur // N, cur % N  # 2차원일 때의 행과 열 계산
            if 0 < r and arr[cur - N] == '0':
                que.append(cur - N)
                arr[cur - N] = '1'
                cnt -= 1
            if r < M - 1 and arr[cur + N] == '0':
                que.append(cur + N)
                arr[cur + N] = '1'
                cnt -= 1
            if 0 < c and arr[cur - 1] == '0':
                que.append(cur - 1)
                arr[cur - 1] = '1'
                cnt -= 1
            if c < N - 1 and arr[cur + 1] == '0':
                que.append(cur + 1)
                arr[cur + 1] = '1'
                cnt -= 1

    return ans if cnt == 0 else -1


if __name__ == '__main__':
    print(solve())
