for _ in range(10):
    T = int(input())
    N = [list(map(int, input().split())) for i in range(100) ]  # 100*100 행렬    
    line_sum, cross_L, cross_R = [],[],[]

    for i in range(len(N)):  # 0~99줄까지
        line_sum.append(sum(N[i]))  # 각 행의 합 line_sum에 추가
        cross_L.append(N[i][i])    # cross_L에 원소 하나씩 뽑아 넣기 
        cross_R.append(N[len(N)-1-i][len(N)-1-i])  # cross_R에 원소 하나씩 뽑아 넣기
        col = []
        for j in range(len(N)):
            col.append(N[j][i])
        line_sum.append(sum(col))      # 각 열의 합 line_sum에 추가
    line_sum.append(sum(cross_L))
    line_sum.append(sum(cross_R))
    print(f'#{T} {max(line_sum)}')
