# 백준 - 182446번
# 답은 맞는데 제출하면 시간초과 


# N - 색종이 장수, M - 쿼리의 개수 
N, M = map(int, input().split())

# 색종이 좌표 입력받기
colored_paper = [list(map(int, input().split())) for _ in range(N)]
# 2차원 list 생성(색종이를 배치할 판 생성)
ary_len = max(sum(colored_paper,[])) 
place = [[0 for _ in range(ary_len)] for _ in range(ary_len)]
# 색종이 배치
for paper in colored_paper:
    for row in range(paper[0], paper[2]):
        for col in range(paper[1], paper[3]):
            place[row][col] += 1

# 쿼리 좌표 입력 받기
query = [list(map(int, input().split())) for _ in range(M)]
# 쿼리 출력
for q in query:
    query_list = []
    for row in range(q[0], q[2]):
        query_list.append(max(place[row][q[1]:q[3]]))
    print(max(query_list))

