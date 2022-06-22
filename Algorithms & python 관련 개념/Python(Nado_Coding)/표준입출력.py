print("Python", "Java", sep=" vs ", end="?\n")
print("무엇이 더 재밌을까요?") 

# ------------------------  1  ------------------------ 
# stdout과 stderr
# stdout : 표준 출력
# - log처리를 한다고 할 경우, 표준 출력에 대해서는 크게 신경 쓸 필요 없음 
# stderr : 표준 에러
# - log처리를 한다고 할 경우, 확인을 해서 code를 수정하던지 해야함
# - 그럴 떄 stderr(표준 에러)로 처리되는 부분에 대해서 따로 logging을 하던 해서 필요에 따라 에러처리를 해줄 수 있음 

from sys import *
print("Python", "Java", file=stdout)
print("Python", "Java", file=stderr)


# ------------------------  2  ------------------------  
# 출력포멧 - ljust와 rjust

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")  
    # ljust(8) : 8개의 공간을 확보한 후 왼쪽 정렬을 해라
    # rjust(4) : 4개의 공간을 확보한 후 오른쪽 정렬을 해라


# ------------------------  3  ------------------------ 
# 은행 대기순번표
# 001, 002, 003
for num in range(1,21) :
    print(f"대기번호 : " + str(num).zfill(3))
    # zfill(3) : 3만큼의 공간을 확보하고 문자를 채운 후 빈 공간을 0으로 채워라


# ------------------------  4  ------------------------ 
# 표준 입력
# - 사용자 입력을 통해서 입력을 받게 되면 항상 문자로 저장됨 

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print(f"입력하신 값은 {answer} 입니다")