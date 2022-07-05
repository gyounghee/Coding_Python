# 5525번 - IOIOI

## 내 풀이
# - 메모리 : 37364 KB  /  시간 : 784 ms

from sys import *
input = stdin.readline

N, M = int(input()), int(input())
S = input().rstrip()
ans = 0
IOIOI = []
for s in S :
    if not IOIOI :  # 비었을 때 
        if s == 'I' : IOIOI.append(s)  # s가 I면 추가
        else : continue   # O면 넘기기
    elif len(IOIOI) == 1 and s == 'I' : continue  # IOIOI에 'I'가 들어있을 때 다음 문자열이 'I'가 나오면 넘김  
    elif len(IOIOI) > 1 and IOIOI[-1] == 'I' and s =='I' : IOIOI = ['I']
    elif IOIOI[-1] != s :  # s가 마지막 문자열과 다르면 
        IOIOI.append(s)    # 추가
        if len(IOIOI) == 2*N+1 :   # 만약 IOIOI가 목표치가 되면 
            ans += 1     # ans + 1 해주고
            IOIOI.pop()  # I 빼줌
            IOIOI.pop()  # O 빼줌
    else :   # 마지막 문자열과 같은 문자열이 나오면
        IOIOI = []  # 문자열 초기화
print(ans)
