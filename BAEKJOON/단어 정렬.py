# 1181번 - 단어 정렬

from sys import stdin

n = [ stdin.readline().strip() for _ in range(int(stdin.readline())) ]
n = list(set(n))
n.sort(key=lambda x: (len(x),x))

for s in n :
    print(s)
