# 15649번 - N과 M (1)

# 내 풀이
from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split())

perm = permutations(list(range(1,N+1)), M) # 순열 생성
for p in perm :
    print(' '.join(map(str, p)))


    
# 강의 풀이
# 1. 아이디어
#   - 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(방무여부 확인)
#   - 재귀함수에서 M개를 선택할 경우 print 
# 2. 시간복잡도
#   - N!
# 3. 자료구조
#   - 결과값 저장(list), 방문여부 체크(list)

from sys import stdin
           
N, M = map(int, stdin.readline().split())  # 두 개의 숫자를 입력
ans = []
chk = [False] * (N+1)

def BT(n) :
    if n == M :
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
        if chk[i] == False :
            chk[i] = True
            ans.append(i)
            BT(n+1)
            chk[i] = False
            ans.pop()
            
BT(0)



