# def is_valid(r, c, N, M):
#     return 0<=r<N and 0<=c<M

# dr = [1, 0]
# dc = [0, 1]

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
    
#     max_cnt = 0
#     visited = [[False]*M for _ in range(N)]

#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1 and not visited[i][j]:
                
#                 for d in range(2):
#                     cnt = 0
#                     ni, nj = i, j
                    
#                     while is_valid(ni,nj,N,M) and arr[ni][nj] == 1:
#                         visited[ni][nj] = True
#                         cnt += 1
#                         ni += dr[d]
#                         nj += dc[d]

#                     if cnt >=2:
#                         max_cnt = max(max_cnt, cnt)
#     print(f'#{tc} {max_cnt}')

def is_valid(r, c, N, M):
    return 0<=r<N and 0<=c<M

dr = [1, 0]
dc = [0, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                
                for d in range(2):
                    cnt = 1
                    ni, nj = i, j

                    while True:
                        ni += dr[d]
                        nj += dc[d]
                        if is_valid(ni,nj,N,M) and arr[ni][nj] == 1:
                            cnt += 1
                        else:
                            break

                    if cnt > max_cnt:
                        max_cnt = cnt

    print(f'#{tc} {max_cnt}')



def is_valid(r, c, N, M):
    return 0<=r<N and 0<=c<M

dr = [1, 0]
dc = [0, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                
                for d in range(2):
                    cnt = 1
                    for k in range(max(N,M)):
                        ni = i + dr[d]*(k+1)
                        nj = j + dc[d]*(k+1)

                        if is_valid(ni,nj,N,M) and arr[ni][nj] == 1:
                            cnt += 1
                        else:
                            break
                    if cnt > max_cnt:
                        max_cnt = cnt
    print(f'#{tc} {max_cnt}')