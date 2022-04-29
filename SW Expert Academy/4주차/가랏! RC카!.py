for c in range(int(input())):
    N = int(input())
    current, total = 0,0
    
    for _ in range(N):
        car = list(map(int, input().split()))
        
        if car[0] == 0 :
            total += current
        elif car[0] == 1 :
            current += car[1]
            total += current
        else : 
            if car[0] > current :
                speed = 0
            else :
                current -= car[1]
                total += current
    
    print(f'#{c+1} {total}')
