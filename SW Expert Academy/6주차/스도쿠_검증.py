for c in range(int(input())):
    sudoku = [list(map(int, input().split())) for i in range(9)] # 스도쿠 만들기
    row, col, box = 0,0,0
    li = []
    # 행, 열 별로 계산
    for i in range(9):
        li = []
        if len(set(sudoku[i])) == 9 : row += 1   # 행의 숫자가 겹치지 않으면 row += 1
        for j in range(9):
            li.append(sudoku[j][i])
        if len(set(li)) == 9 : col += 1          # 열의 숫자가 겹치지 않으면 col += 1
    # 박스로 묶어서 계산
    for i in range(3):
        box_num = []
        for j in range(3):
            box_num = sudoku[i*3][(j*3):(j*3)+3]+sudoku[i*3+1][(j*3):(j*3)+3]+sudoku[i*3+2][(j*3):(j*3)+3]
            if len(set(box_num)) == 9 : box += 1  # 3 X 3 박스 안에 겹치는 숫자가 없으면 box += 1
    if (row + col + box) == 27 : print(f'#{c+1} 1')     # 모두 겹치지 않아서 +1이 27이 되면 "1 출력" 
    else : print(f'#{c+1} 0')    # 겹치는게 있어서 +1 이 27이 되지 못했으면 "0 출력"
