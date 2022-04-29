for c in range(int(input())):
    N, K = map(int, input().split())
    ary = []
    find, kc = 0,0
    for _ in range(N):
        ary.append(input().split())

    for i in range(N):
        kc = 0
        for j in range(N):
            if ary[i][j] == '1' : kc += 1
            elif K == kc and ary[i][j] == '0' :
                find += 1
                kc = 0
            elif ary[i][j] == '0' : kc = 0
        if K == kc :
            find += 1
        kc = 0
        for k in range(N) :
            if ary[k][i] == '1' : kc += 1
            elif K == kc and ary[k][i] == '0' :
                find += 1
                kc = 0
            elif ary[k][i] == '0' : kc = 0
        if K == kc :
            find += 1
    print(f'#{c+1} {find}')
        
