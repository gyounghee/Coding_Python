# 10989번 - 수 정렬하기 3

from sys import stdin, stdout

n = int(stdin.readline())
n_list = [0] * 10001
for _ in range(n):
    n_list[int(stdin.readline())] += 1
  
for i in range(len(n_list)):
    for j in range(n_list[i]):
        if n_list[i] != 0 :
            stdout.write(str(i)+'\n')
