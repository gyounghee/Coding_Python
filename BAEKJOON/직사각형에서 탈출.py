# 1085번 - 직사각형에서 탈출

from sys import stdin

x, y, w, h = map(int, stdin.readline().split())
print(min(x,y, w-x, h-y))
