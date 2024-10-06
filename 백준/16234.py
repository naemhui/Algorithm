'''
r행 c열
L명 이상 R명 이하 -> 국경선 오픈
연합
인구수 : 연합의 인구수 / 연합을 이루는 칸의 개수
연합 해체, 국경선 close
'''
from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 연합을 찾고 연합에 속한 나라들을 저장하는 bfs
def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:

                if L<=abs(graph[nx][ny]-graph[x][y])<=R:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp
            
result = 0  # 인구 이동 발생
while True:
    visited = [[0] * (N+1) for _ in range(N+1)]
    flag = 0  # 인구 이동 발생했는지?
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                if len(country) > 1:
                    flag = 1
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x,y in country:
                        graph[x][y] = number
    if flag == 0:
        break
    result += 1
print(result)
