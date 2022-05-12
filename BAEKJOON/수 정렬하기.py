import heapq

n = int(input())  # 줄의 개수
numbers = []
for _ in range(n):
    heapq.heappush(numbers, int(input()))

for _ in range(len(numbers)):
    print(heapq.heappop(numbers))
