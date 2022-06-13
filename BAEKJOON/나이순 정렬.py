# 10814번 - 나이순 정렬

from sys import stdin

custom = [stdin.readline().split() for _ in range(int(stdin.readline())) ]
custom.sort(key=lambda x: int(x[0]))
for c in custom :
    print(' '.join(c))
