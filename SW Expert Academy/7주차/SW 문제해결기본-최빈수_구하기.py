for _ in range(int(input())):
    c = int(input())     # TEST CASE 번호 입력
    N = list(map(int, input().split()))
    num, mode = {},[]   # num에 숫자 빈도수를 dict 형태로 만듦, mode - 최빈수를 담을 list 생성
    for i in N:   # num에 각 수의 빈도수를 나타냄
        try :
            if num[i] >= 1 : num[i] += 1
        except : num[i] = 1

    for key, value in num.items():  # num의 key와 value를 하나씩 들여다 봄
        if value == max(num.values()):   # 해당 value 값이 빈도수가 가장 큰 value와 같으면
            mode.append(key)        # 최빈값을 담을 그릇에 해당 value의 key값 추가 

    print(f'#{c} {max(mode)}')
