# 15829번 - Hashing

from sys import *

input = stdin.readline
n = int(input())
alpha = input()
total = 0

for i in range(n) :
    total += (ord(alpha[i])-96) * (31**i)

print(total)
