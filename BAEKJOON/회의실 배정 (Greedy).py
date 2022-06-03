# 1931번 - 회의실 배정
# Greedy 알고리즘을 이용한 문제풀이
# - 문제를 잘못 이해해서 푸는데 오래걸렸음ㅜ


### 풀이 1
# - input()으로 입력을 받으니 4252ms의 시간이 걸림

lecture = int(input()) 
lec_info = [ list(map(int, input().split())) for _ in range(lecture) ]
lec_info.sort(key = lambda x : (x[1], x[0]) )

ans = 0
start = 0
for s,e in lec_info:
    if start <= s :
        ans += 1
        start = e
print( ans )




### 풀이 2
# - sys의 stdin.readline()을 사용하면 시간을 320ms까지 줄일 수 있었음

from sys import stdin

lecture = int(stdin.readline())
lec_info = [ list(map(int, map(int,stdin.readline().split()))) for _ in range(lecture) ]
lec_info.sort(key = lambda x : (x[1], x[0]) )

ans = 0
start = 0
for s,e in lec_info:
    if start <= s :
        ans += 1
        start = e
print( ans )
