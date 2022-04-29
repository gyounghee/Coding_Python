from collections import deque

count = int(input())

for c in range(1, count+1) :
    queue_len, rotation = map(int, input().split())
    queue = input().split()
    queue = deque(queue)
    for _ in range(rotation):
        queue.append( queue.popleft() )
    print(f'#{c} {queue[0]}')
