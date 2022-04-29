def sidefind(P):   
    global find
    for i in range(8):    
        for j in range( len(P)-f+1 ):
            select =  P[i][j:j+f]
            if select == select[::-1] : find += 1

def downfind(P): 
    global find
    for i in range(8):  
        for j in range( len(P)-f+1 ):
            select =  []   # 회문의 길이 만큼 행 인덱싱
            for k in range(f):
                select.append(P[j:j+f][k][i])
            if select == select[::-1] : find += 1

for c in range( 10 ):  # 10개의 TEST CASE 
    f = int(input()) # 회문의 길이
    P = [ list(input()) for _ in range(8)] # 8x8 글자판 생성

    find = 0     # 회면 찾으면 +1 하기 위한 변수 생성
    sidefind(P)  # 가로로 찾기
    downfind(P)  # 세로로 찾기   

    print(f'#{c+1} {find}')  # 출력
