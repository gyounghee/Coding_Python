# 2812번 - 크게 만들기

# stack을 이용한 문제 풀이
from sys import stdin

n_len, del_n = map(int, stdin.readline().split())
n = stdin.readline()

delete, stack = del_n, []
i = 0
while delete != 0 and i != n_len :
    if stack and stack[-1] < n[i] :
        delete -= 1
        stack.pop()
    else :
        stack.append(n[i])
        i += 1
        
if len(stack) < n_len :
    stack.append(n[i:])
print( ''.join(i for i in stack)[:(n_len-del_n)] )
