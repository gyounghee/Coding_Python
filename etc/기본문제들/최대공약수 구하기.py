# 최대 공약수 구하기
# * 실행 과정 *
# 1. a, b가 주어졌을 때, b가 a보다 크면 b의 값을 a로, a의 값을 b로 지정한다.
# 2. a를 b로 나눈 나머지를 n으로 지정한다.
# 3. n이 0이면 b가 최대공약수이다. (종료)
# 4. n이 0이 아니라면, a의 값을 b로, b의 값을 n로 지정하고, 2번으로 돌아간다.


a, b = map(int, input().split())

if b >= a : a, b = b, a

while True :
    n = a % b
    if n != 0 :
        a, b = b, n
    else :
        print("최대공약수(GCD)는 ", b)
        break
