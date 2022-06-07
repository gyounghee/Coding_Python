# 10610번 - 30

# 3의 배수가 되려면 각 자리의 수의 합이 3의 배수가 되어야 함을 이
n = list(input())

if not n.count('0') or sum(map(int, n)) % 3 != 0  :
    print(-1)
else :
    n.sort(reverse=True)
    print( int(''.join(n)) )
