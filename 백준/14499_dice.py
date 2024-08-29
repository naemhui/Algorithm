'''
N*M 지도
지도의 좌표: (r, c) : 북쪽부터, 서쪽부터 떨어진 칸의 개수
지도 0 -> 주사위 바닥면 = 지도
지도 n -> 주사위 바닥면 n, 지도 0

현재 주사위: 1, 2, 3, 4, 5, 6
동: 4, 2, 1, 6, 5, 3
서: 3, 2, 6, 1, 5, 4
남: 2, 6, 3, 4, 1, 5
북: 5, 1, 3, 4, 6, 2
'''
def my_dice(command):
    # 동
    if command == 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    # 서
    elif command == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    # 남
    elif command == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]   
    # 북
    elif command == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    
def is_valid(N, M, n, m):
    return 0<=n<N and 0<=m<M

# 세로, 가로, 좌표x, 좌표y, 명령 개수
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
dice = [0, 0, 0, 0, 0, 0]

# 동 1 서 2 북 3 남 4
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

## 여기까지 지도 다 채움

command = list(map(int, input().split()))
for i in range(K):
    command[i] -= 1

# x, y에서 시작함
for k in command:
    x = x + dr[k]
    y = y + dc[k]
    if is_valid(N, M, x, y):
        my_dice(k)
        # 1.지도에 적힌 수가 0
        if arr[x][y] == 0:
            arr[x][y] = dice[5]
        # 2. 지도에 적힌 수가 0이 아니면
        else:
            dice[5] = arr[x][y]
            arr[x][y] = 0
        print(dice[0])
    else:
        x -= dr[k]
        y -= dc[k]