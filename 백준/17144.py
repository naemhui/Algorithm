dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C

# 미세먼지 확산
def spread():
    temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                amount = arr[r][c] // 5
                count = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if is_valid(nr, nc) and arr[nr][nc] != -1:
                        temp[nr][nc] += amount
                        count += 1
                arr[r][c] -= amount * count  # 남은 미세먼지
    # temp -> 원본
    for r in range(R):
        for c in range(C):
            arr[r][c] += temp[r][c]

# 공기청정기
def airpurifier():
    upper = purifier[0]  # 위쪽 
    lower = purifier[1]  # 아래쪽

    # 윗바람 - 반시계
    for r in range(upper - 1, 0, -1):
        arr[r][0] = arr[r - 1][0]

    arr[0][:C - 1] = arr[0][1:]
    arr[0][C - 1] = arr[1][C - 1]

    for r in range(upper):
        arr[r][C - 1] = arr[r + 1][C - 1]

    arr[upper][1:] = arr[upper][:C - 1]
    arr[upper][1] = 0

    # 아랫바람 - 시계
    for r in range(lower + 1, R - 1):
        arr[r][0] = arr[r + 1][0]

    arr[R - 1][:C - 1] = arr[R - 1][1:]

    for r in range(R - 1, lower, -1):
        arr[r][C - 1] = arr[r - 1][C - 1]

    arr[lower][1:] = arr[lower][:C - 1]
    arr[lower][1] = 0


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
purifier = []


for r in range(R):
    if arr[r][0] == -1:
        purifier.append(r)

for _ in range(T):
    spread()
    airpurifier()

dust = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] >0:
            dust += arr[r][c]

print(dust)
