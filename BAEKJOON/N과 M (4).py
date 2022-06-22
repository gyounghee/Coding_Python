# 15652번 - N과 M (4)

from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

rs = []
chk = [False] * (N+1)

def BT(n):
    if n == M :
        print(' '.join(map(str, rs)))
        return
    for i in range(1,N+1):
        if not rs or (not chk[i] and rs[-1] <= i) :
            chk[i] == True
            rs.append(i)
            BT(n+1)
            chk[i] == False
            rs.pop()

BT(0)
