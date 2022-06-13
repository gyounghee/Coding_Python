# 2609번 - 최대공약수와 최소공배수

# 풀이 1
# math의 gcd,lcm 라이브러리 사용
from math import gcd,lcm

a, b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))


## 풀이 2
# - 유클리드 호제법
# - 최소 공배수 = 두 수의 곱 / 최대공약수
x, y = map(int,input().split())
a, b = max(x,y), min(x,y)

while b != 0:
    a,b = b,a%b
    
print(a)
print(x*y//a)
