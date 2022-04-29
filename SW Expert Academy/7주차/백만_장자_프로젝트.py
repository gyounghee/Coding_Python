# Fail (제한시간 초과)  - 10개 중 7개 맞음
for c in range(int(input())):
    day = int(input())
    price = list(map(int, input().split()))
    thing ,money = 0,0
    
    for d in range(day):
        if thing == 0 and price[d] == max(price): price[d] = 0 
        elif price[d] != max(price) :
            thing += 1
            money -= price[d]
            price[d] = 0
        else :
            money += thing * price[d]
            thing,price[d] = 0,0
            
    print(f'#{c+1} {money}')





# 다른 사람 풀이 참고
for c in range(int(input())):   # 총 몇번 실행할지 
    day = int(input())          # 며칠 동안 매매가 이루어지는지 
    price = list(map(int, input().split()))  # 날짜별 매매가
    buy, profit = 0,0           # buy - 최근 구매가, profit - 수익
    
    for p in price[::-1]:       # 제일 마지막 날 부터 살펴봄 
        if p > buy :            # 최근 구매가보다 매매가가 크면
            buy = p
        profit += buy - p       # (최근 구매가 - 현재 매매가) 수익이 되므로 둘의 차액을 수익에 더해줌
            
    print(f'#{c+1} {profit}')
