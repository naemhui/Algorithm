import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = []  # 방문한 알파벳 저장
max_cnt = 0  # 최대 경로 길이

def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C

def dfs(r, c, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if is_valid(nr, nc) and board[nr][nc] not in visited:
            visited.append(board[nr][nc])  # 알파벳 방문 기록
            dfs(nr, nc, cnt + 1)
            visited.pop()  # 방문 기록 제거

visited.append(board[0][0])
dfs(0, 0, 1)

print(max_cnt)