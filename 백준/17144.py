'''
RxC

1. 네 방향 확산
2. 공기청정기 있으면 확산 x
3. 미세먼지//5만큼 확산됨
4. 남은 미세먼지: 확산된 양*확산된 칸
##
1. 공기청정기 작동 : 윗바람 - 반시계, 아랫바람-시계
- 바람 방향대로 미세먼지 이동
'''
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
purifier = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r,c):
    return 0<=r<R and 0<=c<C

for r in range(R):
    for c in range(C):
        if arr[r][c] == -1:
            purifier.append(r)

    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                amount = arr[r][c]//5
                for _ in range(4):
                    nr = r + dr[_]
                    nc = c + dc[_]
                    if is_valid(nr,nc) and arr[nr][nc]!=-1:
                        arr[nr][nc] += amount
                        arr[r][c] -= amount


        # 미세먼지 이동은 방향과 반대 순서로 확인
        # pufifier = [2, 3]
    for _ in range(T):
        # 1. 윗바람
        for r in range(purifier[0]-1, 0, -1):
            arr[r][0] = arr[r-1][0]
        arr[0] = arr[0][1:] + arr[1][-1]
        for r in range(1, purifier[0]):
            arr[r][0] = arr[r+1][0]
        arr[purifier[0]] = [-1, 0] + [purifier[0]][0]

        # 2. 아랫바람
        for r in range(purifier[1]+1, R):
            arr[r][0] = arr[r+1][0]
        arr[R-1] = arr[R-1][1:] + arr[R-1][-1]
        for r in range(R-2, purifier[-1], -1):
            arr[r][C] = arr[r-1][C]
        arr[purifier[1]] = [-1, 0] + arr[purifier[1]][1:C-2] 
        

        # 마지막에 공기청정기가 빨아드린 먼지 제거
        arr[purifier[0]-1][0] = 0
        arr[purifier[1]+1][0] = 0

    # 반시계방향: 우상좌하
    # dr_up = [0, -1, 0, 1]
    # dc_up = [1, 0, -1, 0]
    # # 시계방향: 우하좌상
    # dc_down = [0, 1, 0, -1]
    # dr_down = [1, 0, -1, 0] 

    # def arir_purifier(r,c):
    #     arr[r][c] 

    # d = 0
    # for i in range(2*R+2*C-5):
    #     nr = r + dr_up[d]
    #     nc = c + dc_up[d]
dust = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] >0:
            dust += arr[r][c]

print(arr)