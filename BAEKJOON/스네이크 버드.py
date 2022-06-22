# 16345번 - 스네이크 버드

# - 자신의 길이보다 작거나 같은 높이에 있는 과일을 먹을 수 있음
# - 과일을 먹을 때마다 길이가 1만큼 늘어남

from sys import stdin
from heapq import *

N, L  = map(int, stdin.readline().split())
fruit = list(map(int, stdin.readline().split()))
heapify(fruit)

for _ in range(N):
    f = heappop(fruit)
    if f > L : break
    L += 1

print(L)
