# 1003번 - 피보나치 함수
# DP - 동적프로그래밍을 이용한 문제풀이

def Fibonnaci(n) :
    global fb_list
    if n == 0 :
        return [1,0]
    if n == 1 :
        return [0,1]
    if fb_list[n] != [0,0] :
        return fb_list[n]
    else :
        fb_list[n][0] = Fibonnaci(n-1)[0] + Fibonnaci(n-2)[0]
        fb_list[n][1] = Fibonnaci(n-1)[1] + Fibonnaci(n-2)[1]
        return fb_list[n]
        
for tc in range( int(input()) ) :
    num = int(input())
    fb_list = [[0,0] for _ in range(num+1)]
    zero, one = Fibonnaci( num )[0], Fibonnaci( num )[1]
    print( zero, one )



### 다른 사람 풀이
from sys import stdin
T = int(input())    # Test Case 개수
l = [int(stdin.readline()) for _ in range(T)]  # 한번에 입력받아 list로 저장 
f = [[1, 0], [0, 1]]

for i in range(2, max(l)+1):   # 2부터 입력 받은 수 중 가장 큰 수까지 봐야하기 때문에 max(l)+1  
    f.append([f[i-2][0]+f[i-1][0], f[i-2][1]+f[i-1][1]])

for i in l:
    print(' '.join(map(str, f[i])))  # 해당 번호의 값 들을 공백을 구분자로하여 합침
