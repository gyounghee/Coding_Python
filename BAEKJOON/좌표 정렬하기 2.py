# 11651번 - 좌표 정렬하기 2

from sys import *
input = stdin.readline

dot = [ list(map(int, input().split())) for _ in range(int(input())) ]
dot.sort( key = lambda x : (x[1],x[0]))

for d in dot :
    print(d[0],d[1])
