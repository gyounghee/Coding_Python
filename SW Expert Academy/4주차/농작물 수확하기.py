for c in range(int(input())):
    N = [ list(input()) for _ in range( int(input()) ) ]  
    for i in range(len(N)) :  
        N[i] = list(map(int, N[i]))
    total, h = 0, len(N)//2
    for i in range(h+1):
        total += sum(N[h-i][i:-i])  # 위
        total += sum(N[h+i][i:-i])  # 아래
    total += sum(N[h])# 중간
    print(f'#{c+1} {total}')
