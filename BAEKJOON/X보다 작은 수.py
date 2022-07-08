# 10871번 - X보다 작은 수

from sys import *
input = stdin.readline

N, X = map(int, input().split())
print(' '.join([ str(n) for n in input().split() if int(n) < X ]))
