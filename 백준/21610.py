'''
비바라기 
-> (N,1), (N,2), (N-1,1), (N-1,2)
1. 방향 d 거리 s
2. 구름 : True False
    물: +1
3. 물복사버그(대각선만큼 증가)
4. 물의 양 >= 2이면 구름, 물-2, 
'''
def is_valid(r,c):
    return 1<=r<= N and 1<=c<= N

def be_valid(r,c):
    if r<1:
        r = N - (abs(r) % N)
    elif r > N:
        r = r%N
        if r == 0:
            r = N

    if c<1:
        c = N - (abs(c) % N)
        
    elif c>N:
        c = c%N
        if c == 0:
            c = N
    return r, c

dr = ['N', 0, -1, -1, -1, 0, 1, 1, 1]
dc = ['N', -1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(r,c,d,s):
    # 구름 이동
    nr = r + dr[d]*s
    nc = c + dc[d]*s
    nr, nc = be_valid(nr, nc)
    return nr, nc

def add_water(r,c):
    plus = 0
    for d in range(2, 9, 2):
        nr = r+dr[d]
        nc = c+dc[d]
        if is_valid(nr, nc) and arr[nr][nc]:
            plus += 1

    return plus


N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    arr[i][1:N+1] = map(int, input().split())

# 구름의 상태: 구름이 있는지, 이전에 사라졌는지
cloud = [[False]*(N+1) for _ in range(N+1)]
total_water = 0

initial_cloud = [(N,1), (N,2), (N-1,1), (N-1,2)]
for r, c in initial_cloud:
    cloud[r][c] = True

for _ in range(M):
    d, s = map(int, input().split())
    now_cloud = [[False]*(N+1) for _ in range(N+1)]
    

    # 1.구름 이동
    for r in range(1, N+1):
        for c in range(1, N+1):
            if cloud[r][c]:
                nr, nc = move_cloud(r,c,d,s)
                now_cloud[nr][nc] = True
                # 2.물 증가
                arr[nr][nc] += 1
    cloud = now_cloud

    
    for r in range(1, N+1):
        for c in range(1, N+1):
            if cloud[r][c]:
                arr[r][c] += add_water(r,c)

    for r in range(1, N+1):
        for c in range(1, N+1):
            if arr[r][c] >= 2 and not cloud[r][c]:
                # if cloud[r][c] != False:
                cloud[r][c] = True
                arr[r][c] -= 2
                # 아하!!!!!!!!!!!!!!!!!!!
            elif cloud[r][c]:
                cloud[r][c] = False
    # print(arr)
    # print('###')

for r in range(1, N+1):
    for c in range(1, N+1):
        total_water += arr[r][c]

print(total_water)
# print(arr)
# print('************')
# print(cloud)