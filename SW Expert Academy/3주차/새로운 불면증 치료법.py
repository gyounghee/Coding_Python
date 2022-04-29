# 새로운 불면증 치료

for c in range(int(input())) :            # 입력 받은 만큼 반복
    n = int(input())                      # n을 입력받음 
    num_list = [0,1,2,3,4,5,6,7,8,9]      # 0~9까지 숫자 리스트 생성 
    for t in range(1,999999) :            # 어차피 num_list가 비면 종료할 것이기 때문에 반복 횟수를 크게 잡음 
        if len(num_list) == 0 : break     # num_list가 비었으면 탈출하도록
        for x in list( str(n * t) ):      # 입력받은 수(n) * t 를  문자형으로 형변환 시켜서 list화 시켜서 x에 하나씩 집어넣음
            if int(x) in num_list :       # 만약 num_list에 x가 있다면  
                num_list.remove(int(x))   # num_list에서 x를 제거하도록 함 
                
    print(f'#{c+1} {n*(t-1)}')   # 출력
