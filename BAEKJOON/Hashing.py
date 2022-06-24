# 15829번 - Hashing

from sys import *

input = stdin.readline
n = int(input())
s = input().rstrip()
alpha = {chr(i):i-96 for i in range(97,123)}
total = 0

for i in range(len(s)) :
    total += alpha[s[i]] * (31**i)

print(total%1234567891)
