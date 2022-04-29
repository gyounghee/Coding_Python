for c in range(int(input())):
    change = int(input())
    money = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}

    for i in money.keys():  # 내림차순으로 하나씩 살펴봄
        if change // i :    # 나눠지면  
            money[i] += (change // i)   # 해당 금액의 value를 count += 1
            change -= i * (change // i) # 거스름돈에서 나눠지는 금액 만큼 빼줌
        if change == 0 : break  

    print(f'#{c+1}')
    for i in money.values():
        print(i, end=' ')
    print()
