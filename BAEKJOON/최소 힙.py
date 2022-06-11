from sys import stdin
from heapq import *

heap = []

for _ in range(int(stdin.readline())) :
    n = int(stdin.readline())
    if n == 0 :
        if not heap :
            print(0)
        else :
            print(heappop(heap))
    else :
        heappush(heap, n)
