gun = 10 

def checkpoint(soldiers) :  # 경계근무
    global gun
    gun -= soldiers    # global로 정의하지 않고 gun변수를 사용할 경우, 함수 내의 gun은 지역변수 이기 때문에 "UnboundLocalError" 에러 발생
    print(f"[함수 내] 남은 총 : {gun}")

print(f"전체 총 : {gun}")
checkpoint(2)  # 2명이 경계 근무 나감
print(f"남은 총 : {gun}")



## 일반적으로 전역변수를 많이 쓰게 되면 코드 관리가 어려워지는 등의 불편함이 발생하기 때문에 
##  ** 전역변수를 사용하지 않을 경우  **
def checkpoint_ret(gun, soldiers) :
    gun -= soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

gun = checkpoint_ret(gun,2)
print(f"남은 총 : {gun}")