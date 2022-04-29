def box(N, row, col, M):   # 파리채의 크기만큼의 박스안의 숫자 보기 위함
    b = []
    for i in range(M):
        b += N[row+i][col:col+M]
    return b

for c in range(int(input())):
    N, M = map(int, input().split())
    N = [ list(map(int, input().split())) for _ in range(N)]   # 배열 입력
    total = []

    for row in range( len(N) - M + 1) :    # 어디 행이 박스의 시작점인지
        for col in range( len(N) - M + 1 ):    # 어디 열이 박스의 시작점인지
            total.append(sum( box(N,row, col,M) ))

    print(f'#{c+1} {max(total)}')
