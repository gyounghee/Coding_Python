# 16953번 - A → B

## 아이디어
# 1. while, for문을 통해 stack에 있는 수에 2를 곱해준 수와 뒷자리에 1을 붙인 수를 추가
#   - 단, 목표 숫자를 넘을 시에는 추가하지 않음
# 2. while문이 돌아간 횟수 == 목표 숫자를 위해 계산한 횟수 → 출력

from sys import *
input = stdin.readline

N, M = map(int, input().split())
ans, stack = 1, [N]

while stack and min(stack) < M :
    if M in stack : break
    
    tmp = []
    for n in stack :
        if n*2 <= M : tmp.append(n*2)
        if int(f'{n}1') <= M : tmp.append(int(f'{n}1'))
    ans += 1
    stack = tmp

print(ans if M in stack else '-1')



