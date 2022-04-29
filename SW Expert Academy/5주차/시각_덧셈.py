for c in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())

    h, m = h1 + h2, m1 + m2
    
    if m >= 60 :
        h += 1
        m %= 60

    if h % 12 == 0 :
        h = 12
    else :
        h %= 12 
    
    print(f'#{c+1} {h} {m}')
