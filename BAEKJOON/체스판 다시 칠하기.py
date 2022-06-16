# 1018번 - 체스판 다시 칠하기

def check(box) :
    c = 0
    tmp1, tmp2 = sum(box[::2],[]), sum(box[1::2],[])
    for i in range(len(tmp1)):
        if i % 2 == 0 :
            if tmp1[i] != 'W' : c += 1
            if tmp2[i] != 'B' : c += 1
        else :
            if tmp1[i] != 'B' : c += 1
            if tmp2[i] != 'W' : c += 1
    return min(64-c,c)
            

N, M = map(int, input().split())
b = sum([list(input()) for _ in range(N)], [])
start = sum([[M*i+j for j in range(M-8+1)] for i in range(N-8+1)],[])  # 시작점 list(1차원) 생성
result = []

for s in start :
    tmp = []
    for i in range(0,8) :
        sp = s+M*i
        tmp.append(b[sp:sp+8])
    result.append(check(tmp))

print(min(result))
