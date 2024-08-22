'''
N*N 정사각 보드
사과 -> 뱀 길이 늘어남
벽, 자기 몸 -> 게임 끝
'''
def is_valid(r,c,N):
    return 0<=r<N and 0<=c<N


# 뱀 이동 함수
# def snake(r,c,N,arr):
    


# 우 하 좌 상 (반시계방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())  # 보드 크기
arr = [[False]*N for _ in range(N)]
K = int(input())  # 사과 개수
for _ in range(K):
    r, c = map(int, input().split())  # 사과의 위치
    arr[r-1][c-1] = 1  # 사과 위치에 1 표시

L = int(input())  # 방향 변환 횟수

d = 0  # 시작 방향(우)
hr, hc = 0, 0  # 머리 위치
tr, tc = 0, 0  # 꼬리 위치

# for r in range(N):
#     for c in range(N):

# 뱀의 방향 변환
for _ in range(L):
    X1, C = input().split()  # x초 후 왼(L) 또는 오(D)로 90도 회전
    X = int(X1)
    for x in range(1, X+1):
        nhr = hr + dr[d%4]*x
        nhc = hc + dc[d%4]*x
        #  뱀이 위치한 부분은 True
        arr[nhr][nhc] = True

        # 죽는지 확인 + 사과 확인 + 꼬리, 머리 위치 확인

        # 1. 머리 확인
        # 뱀이 벽에 부딪히면  (아직 뱀 꼬리랑 머리 닿는 거 고려 안 함)
        if is_valid(nhr,nhc,N) == False:
            print(x)
            break
        else:
            arr[nhr][nhc] = False  # 뱀이 지나갔으니 다시 False로 되돌려놓기

            # 사과를 만났다면
            if arr[nhr][nhc] == 1:
                


    # 여기까지 왔다는 건 뱀이 살아있다!는 뜻
    if C == 'D':
        d += 1
    elif C == 'L':
        d += 3



    # 2. 꼬리 확인
    ntr = tr + dr[d%4]*4  


    # if c == D:
    #     d += 1
    #     ni = i + d[dr]
    #     nj = j + d[dc]