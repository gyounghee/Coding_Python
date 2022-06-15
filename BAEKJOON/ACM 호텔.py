# 10250번 - ACM 호텔

for tc in range(int(input())) :
    H, W, N = map(int, input().split())
    a, b = divmod(N,H)

    if a != 0 and b == 0 :
        print(f'{H}0{a}' if len(str(a)) == 1 else f'{H}{a}')
    else  :
        print(f'{b}0{a+1}' if len(str(a+1)) == 1 else f'{b}{a+1}')
