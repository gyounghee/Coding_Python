count = int(input())   # count → 실행 횟수 

for i in range(1,count+1):    # 
    total = 0       # total 변수 0으로 초기화
    numbers = input().split()    # 입력받은 문자들을 numbers에 저장
    for num in numbers:     # num을 하나 씩 보기 위한 반복문 작성 
        if int(num) % 2 == 1:  # num이 홀수면 total에 더해줌
            total += int(num) 
    print(f'#{i} {total}')     # total 출력


