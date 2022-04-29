count = int(input())          # count → 실행 횟수
b_num = [2, 3, 5, 7, 11]      # b_num → 소인수 저장

for i in range(1, count+1):   # 실행 횟수만큼 반복
    num = int(input())        # num → 숫자를 입력 받음 
    s_num = [0] * len(b_num)  # 각 소인수의 지수를 구하기 위한 리스트 생성 : 소인수의 개수만큼 0을 만듦
    for j in range(0, len(b_num)):    # b_num에 저장한 소인수를 하나 씩 봄
        while num % b_num[j] == 0 :   # 해당 소인수로 더이상 나누어떨어지지 않을 때까지 실행
            s_num[j] += 1             # 나누어 떨어질 때마다 지수 + 1
            num //= b_num[j]          # num을 해당 소인수로 나눈 몫으로 갱신

    print(f'#{i}', end =' ')   # 실행 횟수 출력 
    for k in s_num :           # 각 소인수 지수 값을 한 줄로 출력
        print(k,end=' ')
    print( )
            
    
