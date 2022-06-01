# 모든 멤버의 type 변환하기 - map()

def solution(mylist):
    return list(map(int, mylist))


# map() 응용하기
def solution(mylist):
    answer = list(map(len, mylist))
    return answer
