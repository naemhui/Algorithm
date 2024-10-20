from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr,nc):
    return 0<=nr<N and 0<=nc<M

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0

    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c
            
            if is_valid(nr,nc) and visited[nr][nc] == -1:
                if arr[nr][nc] == 0: 
                    visited[nr][nc] = 0
                elif arr[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))


for i in range(N):
    for j in range(M):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            # print('0 ')
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()