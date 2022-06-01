#  flag OR for-else  - flag 대신 for-else 사용하기

# 내 답안 - flag 방식
nums = [int(input()) for _ in range(5)]
mul_num, find = 1, 1 
for n in nums:
    mul_num *= n
    if mul_num**(1/2) == int(mul_num**(1/2)) :
        print("found")
        f = 0
        break
if f :
        print("not found")



# python의 for-else문
import math

if __name__ == '__main__':     # __name__    →  글로벌 변수     
    nums = [int(input()) for _ in range(5)]
    mul_num = 1 
    for n in nums:
        mul_num *= n
        if math.sqrt(mul_num) == int(math.sqrt(mul_num)) :
            print("found")
            break
    else :
        print("not found")



## +) 추가 공부
#  if __name__ == '__main__':
#   - 해당 모듈이 import가 된 경우가 아니라 interpreter에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령어

#  ↑ 참고 자료  <   https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720   >
