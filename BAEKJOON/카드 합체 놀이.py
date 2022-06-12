# 15903번 - 카드 합체 놀이

from sys import stdin 
from heapq import *

n, m = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))
heapify(card)

for _ in range(m) :
    n_sum = heappop(card) + heappop(card)
    heappush(card, n_sum)
    heappush(card, n_sum)

print(sum(card))
