from collections import deque
board = [list(input()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 중력
def gravity():
    for i in range(6):
        for j in range(10, -1, -1):  # 10~0 : 아래 -> 위
            for k in range(11, j, -1):  # 현재 j 밑 빈칸 있나?
                # j에 뿌요 있고 k 빈칸이면 아래로
                if board[j][i] != '.' and board[k][i] == '.':
                    board[k][i] = board[j][i]
                    board[j][i] = '.'
                    break

def bfs(x, y):
    q = deque([(x, y)])
    color = board[x][y]
    connected = [(x, y)]
    visited[x][y] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nx, ny = r + dx[d], c + dy[d]
            # 범위 내, 방문 X, 같은 색깔이면
            if 0 <=nx<12 and 0<=ny<6 and not visited[nx][ny] and board[nx][ny] == color:
                q.append((nx, ny))
                connected.append((nx, ny))
                visited[nx][ny] = 1

    return connected


total = 0
while True:
    flag = 0
    visited = [[0] * 6 for _ in range(12)]
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:  # 뿌요 O, 방문 X
                connected = bfs(i, j)

                # 뿌요가 4개 이상이믄 삭제
                if len(connected) >= 4:
                    flag = 1
                    
                    for r, c in connected:
                        board[r][c] = '.'
    
    if flag == 0:  # 연쇄 끝
        break
    gravity()
    total += 1

print(total)