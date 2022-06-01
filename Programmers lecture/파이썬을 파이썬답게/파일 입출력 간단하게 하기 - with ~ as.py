# 파일 입출력 간단하게 하기 - with ~ as

# 다른 언어에서 'myfile.txt'를 읽기 위해서는 EOF를 만날 때까지, 파일 읽기를 반복
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line: 
        break
    raw = line.split()
    print(raw)
f.close()



# with ~ as 구문
#  - with as 블록이 종료되면 파일이 자동으로 close되므로, 따로 파일을 close하지 않아도 됨.
#  - readlines가 EOF까지만 읽으므로, While문 안에서 EOF를 체크할 필요가 없음
#  - with ~ as 구문은 파일 뿐만 아니라 socket이나 http 등에서도 사용할 수 있음

with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
