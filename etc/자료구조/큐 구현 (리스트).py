import sys

count = int(sys.stdin.readline())
queue = []

for _ in range(count):
    q = sys.stdin.readline().split()
    command = q[0]    # 공백을 구분자로 하여 나눌 때 앞에있는 문자를 명령어로 저장  
    if command == 'push' :             # 명령어가 "push" 일 경우
        queue.append(int(q[1]))          # 큐에 정수 추가
    elif command == 'pop' :            # 명령어가 "pop" 일 경우
        if len(queue) == 0 : print(-1)   # 큐가 비어있으면 -1 출력
        else :                         # 큐가 비어있지 않으면
            print(queue[0])              # 가장 앞에 있는 정수 출력하고
            del queue[0]                 # 그 수를 뺸다
    elif command == 'size' :           # 명령어가 "size" 일 경우
        print(len(queue))                # 큐의 길이 출력
    elif command == 'empty' :          # 명령어가 "empty" 일 경우
        if len(queue) == 0 : print(1)    # 큐가 비어있으면 1 출력
        else : print(0)                  # 큐가 비어있지 않으면 0 출력
    elif command == 'front' :          # 명령어가 'front' 일 경우
        if len(queue) == 0 : print(-1)   # 큐에 들어있는 정수가 없는 경우 -1 출력
        else : print(queue[0])           # 큐가 비어있지 않은 경우 가장 앞에 있는 정수 출력
    elif command == 'back' :           # 명령어가 'back' 일 경우
        if len(queue) == 0 : print(-1)   # 큐에 들어있는 정수가 없는 경우 -1 출력
        else : print(queue[-1])          # 큐가 비어있지 않은 경우 가장 뒤에 있는 정수 출력
