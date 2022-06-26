# 7568번 - 덩치

from sys import *
input = stdin.readline

N = int(input())
s = [ list(map(int, input().split())) for i in range(N) ]
s = [ [i] + v for i, v in enumerate(s) ]
s.sort(key = lambda x : (x[1], x[2]), reverse=True)

for i in range(N) :
    tmp = i+1
    for j in range(i-1,-1,-1) :
        if s[i][1] == s[j][1] or s[i][2] >= s[j][2] :
            tmp -= 1
    s[i] = [s[i][0], s[i][1], s[i][2], tmp]

seq = sum(sorted(s, key=lambda x : x[0]), [])
print( ' '.join(map(str, seq[3::4])) )



## 다른 사람 풀이
N= int(input())

S = [list(map(int, input().split())) for i in range(N)]

for x1, y1 in S:
    result = 1
    for x2, y2 in S:
        if x1 < x2 and y1 < y2:
            result += 1


    print(result, end =' ')
