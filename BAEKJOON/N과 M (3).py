# 15651번 - N과 M (3)

from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

rs = []

def BT(n):
    if n == M :
        print(' '.join(map(str, rs)))
        return
    for i in range(1,N+1):
        rs.append(i)
        BT(n+1)
        rs.pop()

BT(0)




