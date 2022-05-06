* DFS (깊이 우선 탐색)  
  : 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
    - STACK 자료구조 또는 재귀 함수 이용
    - 동작 과정
        1. 탐색 시작 노드를 stack에 삽입하고 방문 처리
        2. stack의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
        3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복
        ```python 
        def dfs(graph, v, visited):
            visited[v] = True
            print(v, end=' ')

            for i in graph[v]:  
                if not visited[i]:
                    dfs(graph, i, visited)
                    
        # 각 노드가 연결된 정보를 표현
        graph = [
            [],
            [2,3,8],
            [1, 7],
            [1, 4, 5],
            [3, 5],
            [3, 4],
            [7],
            [2, 6, 8],
            [1, 7]
            ]

        visited = [False] * 9

        dfs(graph, 1, visited)
        ```  

* BFS (너비 우선 탐색)  
    : 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
    - Queue 자료구조 이용
    - 동작 과정
        1. 탐색 시작 노드를 queue에 삽입하고 방문 처리
        2. queue에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모듀 큐에 삽입하고 방문 처리
        3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
    ```python
    from collections import deque

    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        
        while queue:  # 큐가 빌 때까지 반복
            v = queue.popleft()   
            print(v, end = ' ')

            for i in graph[v]:   # 방문하지 않은 인접한 원소들을 queue에 삽입
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                
    # 각 노드가 연결된 정보를 표현
    graph = [
        [],
        [2,3,8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
        ]

    visited = [False] * 9

    bfs(graph, 1, visited)
    ```


**문제 1 - 음료수 얼려먹기**
```
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라. 

예시 1)
아래와 같은 4 x 5 얼음 틀에서는 총 3개의 아이스크림이 생성된다.

4 5
00110
00011
11111
00000
```

-----------------------------------------------------------------

**< DFS풀이 >**
```python
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice_mold[x][y] == 0 :
        ice_mold[x][y] = 1

        dfs(x-1,y)    # 상
        dfs(x+1,y)    # 하
        dfs(x,y-1)    # 좌
        dfs(x,y+1)    # 우
        return True
    return False

n, m = map(int, input().split())  # N -  행, M - 열

ice_mold = [list(map(int, input())) for _ in range(n)]
ice = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            ice += 1
print(ice)
```

-----------------------------------------------------------------

**문제 2 - 미로 탈출**
```
N x M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
현재 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시된다. 
탈출하기 위해 움직여햐하는 최소 칸의 개수를 구해라. (칸을 셀 때는 시작칸과 마지막 칸을 모두 포함해서 계산하여야 한다.)

예시 1)
아래와 같은 5 x 6 미로에서 최소 이동 칸의 개수는 10칸이다.
(시작 칸과 마지막 칸은 항상 1이다.)

5 6
101010
111111
000001
111111
111111
```

**< BFS 풀이 >**
```python 
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue :  # queue가 빌 때까지 반복
        x, y = queue.popleft()
        for i in range(4):  # 상 하 좌 우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m : # 범위를 벗어나면 무시
                continue
            if maze[nx][ny] == 0 :  # 벽인 경우도 무시
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1 :
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
        #  가장 오른쪾 아래까지의 최단 거리 반환
    return maze[n-1][m-1]
        

n, m = map(int, input().split())  # N -  행, M - 열

maze = [list(map(int, input())) for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]  # 상, 하, 좌, 우

print(bfs(0,0))
```