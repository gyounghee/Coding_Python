# 1049번 - 기타줄

N, M  = map(int, input().split())
brand = [tuple(map(int, input().split())) for _ in range(M)]
brand = list(zip(*brand))

if min(brand[1])*6 < min(brand[0]) :
    print( min(brand[1])*N )
else : 
    s,p = divmod(N, 6)  # s : 세트 가격, p : 낱개 가격
    print( min( min(brand[0])*(s+1), min(brand[0])*s + min(brand[1])*p) )

