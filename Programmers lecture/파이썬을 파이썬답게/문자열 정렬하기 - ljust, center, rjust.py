# 문자열 정렬하기 - ljust, center, rjust

s, n = input().strip().split(' ')
n = int(n)
for b in range(0,n-len(s)+1,(n-len(s))//2) :
    print(' '*b + s )



#  python의 string 메소드 이용 - ljust, center, rjust
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
