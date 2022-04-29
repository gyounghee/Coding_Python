day_31 =[1,3,5,7,8,10,12]
day_30 =[4,6,9,11]

for c in range(int(input())) :
    total = 0
    M1, D1, M2, D2 = map(int, input().split())
    if M1 == M2 : total = D2-D1+1
    else : 
        for m in range(M2-1,M1-1,-1):
            if m in day_31 : total+=31
            elif m in day_30 : total+=30
            else : total+= 28
        total = total - D1 + D2 + 1
    print(f'#{c+1} {total}')
    
