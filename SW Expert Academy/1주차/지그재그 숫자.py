count = int(input())   # count → 실행횟수

for i in range(1, count+1) :   # 실행 횟수만큼 반복
    num = int(input())         # num → 숫자 입력 받음
    total = 0                  # total → 총합
    for j in range(1, num+1):  # 1부터 num까지 j에 넣음
        if j % 2 == 0 :        # j가 짝수면 totla에서 j만큼 빼고 
            total -= j         
        elif j % 2 == 1 :      # j가 홀수면 total에 j만큼 더한다.
            total += j            
    print(f'#{i} {total}')     # total을 출력
