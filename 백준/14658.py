'''
별똥별 수 최소화
트램펄린 L*L
'''
# N: 가로, M: 세로, L:트램펄린 한 변, K:별똥별 수
N, M, L, K = map(int, input().split())
arr = [[0]*(N+1) for _ in range(M+1)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[y][x] = 1
# print(arr)
# 시계방향으로 굴러가게(달팽이st)
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_valid(r,c, nr, nc):
    return r<=nr<L+r and c<=nc<L+c


max_v = 0
for r in range(M+1):
    for c in range(N+1):
        # 별 있으면 탐색 (모든 점에서 탐색 X)
        if arr[r][c] == 1:
            d = 0
            cnt = 1
            sum_v = arr[r][c]
            # while 1:
            for i in range(L*L):
                if cnt == L*L:
                    max_v = max(max_v, sum_v)
                    break
                nr = r + dr[d]
                nc = c + dc[d]
                print(d)
                # cnt += 1
                if is_valid(r,c,nr,nc) and 0<=nr<=M and 0<=nc<=N: # 다음 위치 유효하면
                    r, c = nr, nc  # 그대로 진행
                    cnt += 1

                else:
                    d = d + 1 if d < 3 else 0
                    r = r + dr[d]
                    c = c + dc[d]
                    cnt += 1
            
print(max_v)

# 상하좌우 순서
# dr = [0, 1, 0, -1]  # 행
# dc = [1, 0, -1, 0]  # 열

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     snail = [[0]*N for _ in range(N)]

#     r, c = 0, 0  # 출발 위치
#     d = 0  # 방향 인덱스

#     for i in range(1, N*N+1):
#         snail[r][c] = i  # 달팽이 1부터 채워짐

#         # 다음 행렬 인덱스
#         nr = r + dr[d]  # 다음 행 인덱스
#         nc = c + dc[d]  # 다음 열 인덱스

#         # 유효 인덱스 검사
#         if 0 <= nr <N and 0 <= nc < N and snail[nr][nc] == 0: # 다음 위치 유효하면
#             r, c = nr, nc  # 그대로 진행

#         else:
#             d = d + 1 if d < 3 else 0  # 유효한 인덱스가 되도록(d는 0, 1, 2, 3)
#             r = r + dr[d]
#             c = c + dc[d]

#     print(f'#{tc}')

#     for i in range(N):
#         print(*snail[i])

