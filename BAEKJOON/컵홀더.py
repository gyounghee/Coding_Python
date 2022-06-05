# 2810번 - 컵홀더

cust = int(input())  # 고객 수
seat = input()    # 좌석 정보

# 좌석에 컵홀더 배치를 포함
seat = seat.replace('S','*S*').replace('LL','*LL*').replace('**','*')
# cup_holder(컵홀더 개수)
cup_holder = seat.count('*')

print( min(cust, cup_holder) )
