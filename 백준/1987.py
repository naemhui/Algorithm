R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = []
max_cnt = 0
r, c = 0, 0  # 시작 위치

def is_valid(r, c):
    return 0<=r<R and 0<=c<C

def dfs(cnt):
    global max_cnt, r, c
    max_cnt = max(max_cnt, cnt)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if is_valid(nr, nc) and board[nr][nc] not in visited:
            visited.append(board[nr][nc])
            # 현재 위치 업데이트 후 dfs
            prev_r, prev_c = r, c  # 이전 위치 저장
            r, c = nr, nc
            dfs(cnt + 1)
            r, c = prev_r, prev_c  # 원래 위치로 되돌리기
            visited.pop()

visited.append(board[0][0])  # 시작 칸 알파벳 추가
dfs(1)

print(max_cnt)
