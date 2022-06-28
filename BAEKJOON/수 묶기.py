# 1744번 - 수 묶기

### 고려해야할 상황
## 계산
# - a, b 모두 1인 경우 → 더해줌
# - a, b 모두 -1인 경우 → 곱해줌
# - a > 1, b <= 1 일 경우 → a는 그냥 더해주고 b는 다시 집어넣음 
# - (a > 1, b > 1) 이거나 (a < 0, b < 0) 이거나 (a < 0, b == 0)

from sys import *
input = stdin.readline

n = [ int(input()) for _ in range(int(input())) ]
res = 0

# 최대값이 양의 정수일 경우 오름차순, 최대값이 0일 경우 내림차순 정렬
n.sort() 
while len(n) > 1 :
    if max(n) < 1 : n.sort(reverse=True)
    a, b = n.pop(), n.pop()
    # 둘다 1인 경우는 더해줌
    if a == 1 and b == 1 : res += 2
    elif a > 1 and b > 1 or a < 0 and b < 0 or a < 0 and b == 0:
        res += a*b
    elif a > 0 and b <= 1 :
        res += a
        n.append(b)
        
print( res+n[0] if n else res )
