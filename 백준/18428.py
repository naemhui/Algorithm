N = int(input())
graph = [list(input().split()) for _ in range(N)]
teacher = []
flag = False

for i in range(N):
    for j in range(N):
        if graph[i][j] == "T":
            teacher.append([i, j])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs():
    for t in teacher:
        for d in range(4):
            nr, nc = t
            while is_valid(nr, nc):
                if graph[nr][nc] == "O":
                    break
                # 학생 보이면 실패
                if graph[nr][nc] == "S":
                    return False
                nr += dr[d]
                nc += dc[d]
    # 모두 통과하면 학새이 안 보인다는 것 => 성공
    return True

def backTracking(cnt):
    global flag

    if cnt == 3:
        # 선생님 위치에서 감시
        if bfs():
            flag = True 
        return
    
    for r in range(N):
        for c in range(N):
            if graph[r][c] == "X":
                graph[r][c] = "O"      # 장애물 설치
                backTracking(cnt + 1)  # 다음 장애물 설치
                graph[r][c] = "X"      # 원래 상태로 되돌리기
                
                if flag:  # 성공하면 빠져나오기
                    return

backTracking(0)

if flag:
    print("YES")
else:
    print("NO")