'''
육지 L 바다 W
상하좌우 델타 함색
'''
from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]


dx=[-1 ,1, 0, 0]
dy=[0, 0, -1, 1]

def is_valid(x, y):
    return 0<=x<N and 0<=y<M

def bfs(i,j):
    q =deque()
    q.append((i,j))
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1

    time = 0
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if is_valid(nx, ny):
                if arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    time = max(time, visited[nx][ny])
                    q.append((nx,ny))            

    return time -1

answer = 0
for r in range(N):
    for c in range(M):
        if arr[r][c]=='L':
            answer = max(answer, bfs(r, c))

print(answer)