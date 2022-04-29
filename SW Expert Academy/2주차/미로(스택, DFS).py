## !! 꼭 다시 풀어보기 !!

def dfs(row, col):
    global path
    array[row][col] = 2
    for p in range(4) : # 상화좌우 확인
        xx = col_check[p] + col
        yy = row_check[p] + row
        if ( xx >= 0 and xx < L ) and ( yy >= 0 and yy < L ) :
            if array[yy][xx] == 0 :  # 만약에 길이 있으면
                dfs(yy,xx)           # 다시 탐색
            if array[yy][xx] == 3 :  # 3을 찾으면 path 1로 바꿔줌
                path = 1
                return path

count = int(input())

for c in range(1,count+1):
    # 미로 생성
    L = int(input())   # 미로 길이
    array = [ ]   
    for _ in range(L):
        ary = input()   
        array.append(list(ary)) 

    # 시작점과 끝 유무 확인
    start, end = 0, 0
    for i in range(L):
        for j in range(L):
            array[i][j] = int(array[i][j])
            if array[i][j] == 2 :
                start = 1
                row, col = i, j   # 시작 행과 열 저장
            if array[i][j] == 3 :
                end = 1

    path = 0  #   길의 유무를 나타내기 위한 변수
    if start & end : # 시작과 끝이 존재한다면 탐색 시작

        # 상하좌우를 다 확인하기 위해
        row_check = [1,-1,0,0]
        col_check = [0,0,1,-1]
        
        dfs(row, col)
        print(f'#{c} {path}')

    else : # 시작과 끝이 존재하지 않는다면 0 출력
        print(f'#{c} {path}')
    
