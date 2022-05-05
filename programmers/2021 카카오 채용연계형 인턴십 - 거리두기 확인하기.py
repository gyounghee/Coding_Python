from collections import deque

dx, dy = [-1,1,0,0], [0,0,-1,1]  # 상하좌우

def bfs(place, i, j):
    visit = [[0]*5 for _ in range(5)]
    q = deque()
    q.append((i,j,0))
    visit[i][j] = 1

    while q :
        x, y, dist = q.popleft()
        if 0 < dist < 3 and place[x][y] == 'P':
            return False   # 멘헤튼 거리가 2 이하면 False 리턴
        if dist > 2 :
            break
        for k in range(4) :   # 상하좌우 탐색
            nx, ny, nd = x + dx[k], y + dy[k], dist + 1
            if 0 <= nx < 5 and 0 <= ny < 5 : # 범위 안에서만 움직이도록
                if place[nx][ny] != 'X' and not visit[nx][ny] :
                    q.append((nx, ny, nd))
                    visit[nx][ny] = 1
    return True
    
def solution(places):
    answer = []

    for place in places :
        chk = 0
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        answer.append(0)
                        chk = 1
                        break
            if chk:   
                break
        else :
            answer.append(1)
    return answer


# TEST CASE Ⅰ
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

