# 1715번 - 카드 정렬하기

from sys import stdin
from heapq import * 

numbers = [ int(stdin.readline()) for _ in range(int(stdin.readline()))]
heapify(numbers) # heapify()에 리스트를 인자로 넘기면 리스트 내부의 원소들의 위에서 다룬 힙 구조에 맞게 재배치되며 최소값이 0번째 인덱스에 위치됨
total = 0

for _ in range(len(numbers)-1) :
    value = heappop(numbers) + heappop(numbers)
    total += value
    heappush( numbers, value )

print(total)
