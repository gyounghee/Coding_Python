# 러시아 농부의 곱셈
# 왼쪽에 있는 수는 2로 나눠주고, 나머지는 버린다. (1이 될때까지 반복)
 #오른쪽에 있는 수는 두배를 해준다.
# 왼쪽에 있는 수가 홀수인 오른쪽의 수들을 모두 더해준다.

# * 예시 *
# 123 x 12
# 61 x 24
# 30 x 48
# 15 x 96
# 7 x 192
# 3 x 384
# 1 x 768

left, right = map(int, input().split())
sum = 0
while True:
    if left % 2 == 1 : sum += right
    if left == 1 : break
    left //= 2
    right *= 2
print('왼쪽이 홀수인 오른쪽 수 들의 합은',sum,'이다')
