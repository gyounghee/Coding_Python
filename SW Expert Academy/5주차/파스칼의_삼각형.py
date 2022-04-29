for c in range(int(input())):
    ary = []
    for i in range(int(input())):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i :  tmp.append(1)
            else :  tmp.append(ary[i-1][j-1]+ary[i-1][j])
        ary.append(tmp)

    print(f'#{c+1}')
    for i in range(len(ary)):
        for j in range(len(ary[i])):
            print(ary[i][j], end=' ')
        print()
