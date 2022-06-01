# 2차원 리스트 뒤집기 - ★ zip ★

def solution(mylist):
    answer = [[] for _ in range(len(mylist[0])) ]
    for n in mylist:
        for i in range(len(n)) :
            answer[i].append(n[i])
    return answer


# zip()과 *(unpacking)을 이용
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))


## zip() 함수
### - zip(*iterables)는 각 iterables 의 요소들을 모으는 iterator를 만듦
### - tuple의 iterator를 돌려주는데, i 번째 tuple은 각 인자로 전달된 시퀀스나 iterable의 i 번째 요소를 포함

mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

# 출력 결과
# (1, 40)
# (2, 50)
# (3, 60)


# zip()의 사용 예 1 - 여러 개의 Iterable 동시에 순회할 때 사용
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)


# zip()의 사용 예 2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
