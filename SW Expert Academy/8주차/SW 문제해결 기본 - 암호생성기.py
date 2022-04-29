for _ in range(10):
    TC = int(input())
    p = list(input().split())

    while int(p[-1]) :
        for i in range(1,6):
            if int(p[-1]) <= 0 :
                p[-1] = "0"
                break
            p.append( str( int(p.pop(0))-i ) )
    
    print(f"#{TC} {' '.join(p)}")
