# 9237번 - 이장님 초대

from sys import stdin

# N : 묘목 수, T : 나무가 자라는데 걸리는 시간
N ,T = int(stdin.readline()), list(map(int, stdin.readline().split()))

T.sort(reverse=True)
day = [ T[i]-(N-i) for i in range(N) if T[i]-(N-i) >= 0]

print(max(day)+N+2)
