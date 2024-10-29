# 1. 감시 체크
def check() :
    for x, y in teacher :
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
            for d in range(1, N) :
                nx= x + dx*d
                ny = y+ dy*d

                # 맵을 벗어나거나 장애물을 마주칠 경우 break
                if (nx < 0 or nx >= N or ny < 0 or ny >= N) or graph[nx][ny] == "O":
                    break
                # 학생이 있을 경우 False
                if graph[nx][ny] == "S":
                    return False
    return True

# 2. 백트래킹
def backtracking(cnt, idx) :
    if idx == len(empty) : return
    # 장애물이 모두 설치된 경우
    if cnt == 3 :
        # 감시를 모두 피할 경우 YES 출력 후 종료
        if check() :
            print("YES")
            exit()
        return

    for i in range(idx, len(empty)):
        x, y = empty[i]
        # 장애물 설치
        graph[x][y] = "O"
        backtracking(cnt + 1, i+1)
        # 장애물 회수
        graph[x][y] = "X"

N = int(input())
graph = [list(input().split()) for _ in range(N)]

teacher, empty = [], []
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == "T" : teacher.append((i, j))
        elif graph[i][j] == "X" : empty.append((i, j))

backtracking(0, 0)
print("NO")