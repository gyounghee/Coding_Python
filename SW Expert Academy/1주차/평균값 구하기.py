count = int(input())   # count → 실행 횟수 

for i in range(1,count+1):       # 실행 횟수만큼 반복
    total, avg = 0, 0            # 총합과 평균을 저장할 변수들을 0으로 초기화
    numbers = input().split()    # numbers에 숫자 여러 개 입력받음
    for j in numbers:            
        total += int(j)          # j들을 더하여 total을 구함
    avg = total / len(numbers)   # 총합을 numbers의 요소들의 개수로 나눠 평균을 구함
    print(f'#{i} {round(avg)}')  # 평균을 반올림하여 출력


