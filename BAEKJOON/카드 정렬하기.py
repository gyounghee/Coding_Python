# 1715번 - 카드 정렬하기

import heapq

numbers = [ int(input()) for _ in range(int(input()))]
numbers.sort()
total = 0

while len(numbers) != 1 :
    one, two = heapq.heappop(numbers), heapq.heappop(numbers)
    total += one + two
    heapq.heappush( numbers, one+two )

print(total)
