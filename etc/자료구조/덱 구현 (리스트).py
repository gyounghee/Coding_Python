import sys

count = int(sys.stdin.readline())
deque = []

for i in range(count):
    dq = sys.stdin.readline().split()
    command = dq[0]

    if command == 'push_front' :
        deque.insert(0,int(dq[1]))
    elif command == 'push_back' :
        deque.append(int(dq[1]))
    elif command == 'size' : print(len(deque))
    elif command == 'empty' :
        if len(deque) == 0 : print(1)
        else : print(0)
    else :
        if len(deque) == 0 : print(-1)
        else :
            if command == 'pop_front' :
                print(deque[0])
                del deque[0]
            elif command == 'pop_back' :
                print(deque[-1])
                del deque[-1]
            elif command == 'front' : print(deque[0])
            elif command == 'back' : print(deque[-1])
