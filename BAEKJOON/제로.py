# 10773번 - 제로

from sys import *
input = stdin.readline

stack = []
for _ in range(int(input())) :
    n = int(input())
    if n == 0 :
        stack.pop()
    else :
        stack.append(n)

print(sum(stack))
