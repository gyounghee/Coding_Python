## 다시 풀어보기
for c in range(int(input())):
    N_len = int(input())
    N = [[0 for _ in range(N_len)] for _ in range(N_len)]

    x, y, i, j = 0, -1, 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(1, pow(N_len,2)+1):
        x += dx[j]
        y += dy[j]
        N[x][y] = i
        if i == N_len or i == (2*N_len)-1 or i == (3*N_len)-2 or N[x+dx[j]][y+dy[j]] != 0 :
            if j == 3 : j = 0
            else : j += 1
    
    print(f'#{c+1}')
    for i in N :
        print(*i)
