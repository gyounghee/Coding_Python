def Insert(cryptogram, loc, c, s):
    tmp = []
    tmp += cryptogram[:loc]
    tmp += s
    tmp += cryptogram[loc:]
    return tmp

def Delete(cryptogram, loc, c):
    tmp = []
    tmp += cryptogram[:loc]
    tmp += cryptogram[loc+c : ]
    return tmp

for tc in range(10):
    cryptogram_len = int(input())  # 원본 암호문의 길이
    cryptogram = input().split()
    command_c = int(input())
    command = input().split()

    for i in range(len(command)):
        if command[i] not in ['I','D','A'] : pass
        else : 
            if command[i] == 'I' :
                loc = int(command[i+1])  # 어느 위치에
                c = int(command[i+2])  # 몇 개의 숫자 넣을건지
                s = command[i+3 :i+3+c]
                cryptogram = Insert(cryptogram, loc, c, s)
            elif command[i] == 'D' :
                loc = int(command[i+1])  # 어느 위치부터
                c = int(command[i+2])  # 몇 개의 숫자를 삭제할건지
                cryptogram = Delete(cryptogram, loc, c)
            elif command[i] == 'A' :
                c = int(command[i+1])  # 몇 개의 숫자 추가할건지
                cryptogram += command[i+2:i+2+c+1]
            
    print(f"#{tc+1} {' '.join(cryptogram[:10])}")
