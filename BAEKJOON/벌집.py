# 2292번 - 벌집

from sys import *

input = stdin.readline
n = int(input())
f, total = 1, 1

while total < n :
    total += 6*f
    f += 1

print(f)
