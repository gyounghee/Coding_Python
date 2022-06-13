# 2869번 - 달팽이는 올라가고 싶다

from sys import stdin
from math import ceil  # 올

A, B, V = map(int, stdin.readline().split())
need = V - A
print( ceil( need/(A-B) ) + 1 )

