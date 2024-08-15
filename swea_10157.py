'''
R X C
행 R, 열 C

엇 이거 달팽이 문제네
'''
# def is_vaild(x, y):
#     return 0<=x<R and 0<=y<C and 

#     상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())
arr = list([0]*C for _ in range(R))

if K > R*C:
    print(0)

else:
    r, c = R-1, 0
    d = 0

    for i in range(1, K+1):
        arr[r][c] = i
        if i == K:
            print(c+1, R-r)
            break

        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<R and 0<=nc<C and arr[nr][nc]==0:
            r, c = nr, nc
        else:
            d = (d+1) % 4
            r = r + dr[d]
            c = c + dc[d]
    
# print(c+1, R-r)