# 11866번 - 요세푸스 문제 0

# 내 풀이
# - Deque 이용
from collections import deque

N, K = map(int, input().split())

n = deque(list(range(1,N+1)))
i, ans = 1, []

while n :
    if i != K :
        n.append(n.popleft())
        i += 1
    else :
        ans.append(n.popleft())
        i = 1

print(f'<{ans}>'.replace('[','').replace(']',''))



## 다른 사람 풀이
# - 나머지 값 이용
N, K = map(int, input().split())

l = list(range(1, N+1))
p = list()
i = 0

while l:
    i = (i+K-1) % len(l)
    p.append(str(l.pop(i)))

print('<'+', '.join(p)+'>')
