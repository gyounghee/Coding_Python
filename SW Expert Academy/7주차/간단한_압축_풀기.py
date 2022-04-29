for c in range(int(input())):
    zip_c = int(input())
    zip = []
    for _ in range(zip_c):
        Ci, Ki = input().split()
        zip += Ci*( int(Ki) )    # zip파일에 다 넣어놓고

    print(f'#{c+1}')
    for i in range(len(zip)):    # 10개씩 끊어서 출력
        if i != 0 and i % 10 == 0 :   # 0번째를 제외하고 10번째일때마다 줄바꿈하고 출력
            print(f'\n{zip[i]}', end='')
        else : print(zip[i], end='')  # 10번째가 아닐때는 그냥 붙여서 출력
    print()
