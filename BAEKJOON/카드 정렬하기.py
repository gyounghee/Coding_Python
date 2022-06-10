# 1715번 - 카드 정렬하기

from sys import stdin
from heapq import * 

numbers = [ int(stdin.readline()) for _ in range(int(stdin.readline()))]
heapify(numbers)
total = 0

for _ in range(len(numbers)-1) :
    value = heappop(numbers) + heappop(numbers)
    total += value
    heappush( numbers, value )

print(total)
