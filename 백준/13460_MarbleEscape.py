'''
파랑+빨강 구슬 넣고 빨간 구슬 빼내야됨
세로 N* 가로 M
4가지 동작 가능: 왼, 오, 위, 아래
구슬이 더 이상 움직이지 않을 때 그만!!
'''

# 기억할 것: 이 함수는 다른 공이 있는 걸 판단하진 못함
def is_valid(i,j,N,M):
    return 1<=i<N-1 and 1<=j<M-1 and arr[i][j] != '#'

# 벽 또는 다른 공 나올 때까지 구슬 이동하는 함수
def roll(i,j):



di = [-1, 1, 0, 0]
dj = [0, 0, -1, -1]

def navi(i, j, color):
    for c in ['R', 'B']:
        if 'c' != color:
            other = c

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if is_valid(ni,nj,N,M):
            while True:
                if arr[ni][nj] == '#':
                    break
                elif arr[ni][nj] == other:
                    # 이전 위치
                    arr[i][j] = color

                    break
                elif arr[ni][nj] == '.':
                    ni += di[d]
                    nj += dj[d]
                # 구멍으로 탈출하면!!!
                else:
                    break
        navi(i,j,color)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# . 빈칸 / # 벽 / o 구멍 / R 빨강 / B 파랑

# 구멍의 위치
for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] == 'O':
            hole_i, hole_j = i, j