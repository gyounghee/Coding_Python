# 11279번 - 최대 힙

from sys import stdin
from heapq import *

input = stdin.readline
h = []
heapify(h)

for i in range(int(input())):
    n = int(input())
    if n == 0 and not h : print(0)
    elif n == 0 and h :
        print(-heappop(h))
    else :
        heappush(h, -n)
