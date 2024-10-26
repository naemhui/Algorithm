'''
상 하 좌 우

'''
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
    return 0<=r<N and 0<=c<N

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

    # 모두 통과하면 학생이 안 보인다는 것 => 성공
    return True


def backTracking(cnt):
    global flag

    if cnt == 3:
        # 선생님 위치에서 감시
        if bfs():
            flag = True  # 성공하면
            return
        
    else:
        # 모든 빈공간에 장애물을 3개씩 설치하기
        for r in range(N):
            for c in range(N):
                if graph[r][c] == "X":
                    graph[r][c] = "O"
                    backTracking(cnt + 1)  # 백트래킹
                    graph[r][c] == "X"


backTracking(0)

if flag:
    print("YES")
else:
    print("NO")