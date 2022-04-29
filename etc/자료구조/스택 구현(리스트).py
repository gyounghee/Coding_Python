# 스택
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오
# * push X: 정수 X를 스택에 넣는 연산이다.
# * pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# * size: 스택에 들어있는 정수의 개수를 출력한다.
# * empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# * top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


import sys

count = int(sys.stdin.readline())
li = []

for _ in range(count):
    a = sys.stdin.readline().split()
    word = a[0]

    if word == 'push':
        li.append(int(a[1]))
    elif word == 'pop':
        if len(li) == 0 : print('-1')
        else :
            print(li[-1])
            li.pop()
    elif word == 'size' : print(len(li))
    elif word == 'empty' :
        if len(li) == 0 : print('1')
        else : print('0')
    elif word == 'top' :
        if len(li) == 0 : print('-1')
        else : print(li[-1])


# 이때, input() 함수를 사용할 경우, 시간초과 에러가 뜬다.
# 시간단축을 위해 sys.stdin.readline()을 사용한다.
# 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
# sys.stdin.readline()을 사용하기 위해 sys도 import 해줬다.
