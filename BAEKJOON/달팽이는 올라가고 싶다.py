# 2869번 - 달팽이는 올라가고 싶다

## 풀이 1
from sys import stdin
from math import ceil  # 올

A, B, V = map(int, stdin.readline().split())
need = V - A
print( ceil( need/(A-B) ) + 1 )


## 풀이 2
A, B, V = map(int, input().split())

print( (V-A)//(A-B) + 1 if (V-A)%(A-B) == 0 else (V-A)//(A-B) + 2 )
