def is_valid(i,j,N):
    return 0<= i < N and 0<= j < N

T = int(input())

for tc in range(1, T+1):
    # N:한 변의 길이, X: 경사로의 길이
    N, X = map(int, input().split())
    arr = [list(map, int(input().split())) for _ in range(N)]

    cnt = 0

    # 경사 낮아지고 있을 때
    for i in range(N):
        for j in range(N):


    # 경사 높아지고 있을 때