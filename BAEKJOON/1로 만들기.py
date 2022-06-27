# 1463번 - 1로 만들기

## 아이디어
# 1. while, for문을 통해 stack에 가능한 계산을 이용하여 계산한 수를 stack에 추가

#  사용 메모리 : 110952 KB  /  시간 688 ms

from sys import *
input = stdin.readline

N = int(input())
ans, stack = 0, [N]

while 1 not in stack :
    tmp = []
    for n in stack :
        if n % 3 == 0 : tmp.append(n//3)
        if n % 2 == 0 : tmp.append(n//2)
        tmp.append(n-1)
    ans += 1
    stack = tmp

print(ans)


### 다른 사람 풀이
#  사용 메모리 : 30840 KB  /  시간 72 ms

l = {int(input())}
n = 0

while 1 not in l :
    t = set()
    n += 1
    for i in l :
        if i % 3 == 0 : t.add(i//3)
        if i % 2 == 0 : t.add(i//2)
        t.add(i-1)   # set에 추가할 때는 add
    l = t
print(n)

# ----------------------------------------------------------------------
## 내 풀이와 다른 점 - 자료형
# - 집합 연산인 set()을 사용한 경우에는 list()에 비해 순서를 보장하지 않아도 되기 때문에 O(1)에 끝나는 연산들이 더 많음
# - 순서를 보장하지 않아도 되는 경우 list() 대신 set()타입을 사용하여 시간 복잡도를 줄일 수 있음
