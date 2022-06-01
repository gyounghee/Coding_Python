# i번째 원소와 i+1번째 원소 - zip()

def solution(mylist):
    return [abs(mylist[i]-mylist[i+1]) for i in range(len(mylist)-1)]

## zip() 이용
def solution(mylist):
    answer = []
    for x, y in zip(mylist, mylist[1:]):
        answer.append(abs(x-y))
    return answer

# - zip() 함수에 서로 길이가 다른 list가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 iteration이 이루어짐

# +) 공식 레퍼런스 - zip()
#  - https://docs.python.org/3/library/functions.html?highlight=built%20function#zip
