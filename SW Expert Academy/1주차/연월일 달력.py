count = int(input())   # count변수에 실행 횟수를 입력받음

month_31 = ['01','03','05','07','08','10','12']  # 31일인 달을 저장
month_30 = ['04','06','09','11']    # 30일인 달을 저장

for i in range(1,count+1):   # 실행 횟수만큼 반복
    date = input()           # date함수에 년원일을 문자열로 입력받음
    # 월에 해당하는 위치에 적혀있는 수가 month_31일에 포함되고, 일에 해당하는 부분이 1~31일 사이에 있으면 출력
    if date[4:6] in month_31 and ( int(date[6:]) >= 1 and int(date[6:]) <= 31 ) :   
        print(f'#{i} {date[:4]}/{date[4:6]}/{date[6:]}')
    # 월에 해당하는 위치에 적혀있는 수가 month_30일에 포함되고, 일에 해당하는 부분이 1~30일 사이에 있으면 출력
    elif date[4:6] in month_30 and ( int(date[6:]) >= 1 and int(date[6:]) <= 30 ) :  
        print(f'#{i} {date[:4]}/{date[4:6]}/{date[6:]}') 
    # 월에 해당하는 위치에 적혀있는 수가 '02'이고, 일에 해당하는 부분이 1~28일 사이에 있으면 출력
    elif date[4:6] == '02' and ( int(date[6:]) >= 1 and int(date[6:]) <= 28 ) : 
        print(f'#{i} {date[:4]}/{date[4:6]}/{date[6:]}')  
    else :   # 형식에 맞지 않거나 값이 이상하면 -1 출력
        print(f'#{i} -1')    
