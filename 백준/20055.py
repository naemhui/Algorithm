# 컨베이어 벨트 위의 로봇
'''
인덱스 조정
N-1, N
N-2, N+1

'''
def conveyor(N, K, arr):
    # idxs = list(range(N)) + list(range(N-1, -1, -1))
    idxs = [list(range(N)), list(range(N-1,-1,-1))]
    robot = [[False]*N for _ in range(2)]
    
    while True:
        # 컨베이어 벨트 회전
        for i in range(2):
            for j in idxs[:-1]:
                if robot[i][j]:
                    robot[i][j] = False
                    robot[i][j+1] = True
        robot[1][0] = False

        # 로봇 이동
        for i in range(2):
            for j in idxs[:-1]:
                if robot[i][j] and robot[i][j+1] != True:
                    # 내구도가 1 이상인 경우에만 이동
                    if i == 0 and arr[i][idxs[j+1]] > 0:
                        robot[i][j] = False
                        robot[i][idxs[j+1]] = True
                        arr[i][idxs[j+1]] -= 1
                    elif i == 1 and arr[i][2*N-1 - idxs[j+1]] > 0:
                        robot[i][j] = False
                        robot[i][idxs[j+1]] = True
                        arr[i][2*N-1 - idxs[j+1]] -= 1

        # 로봇 올리기
        if arr[0][0] != 0:
            robot[0][0] = True
            arr[0][0] -= 1

        # 내구도가 0인 칸
        cnt = sum(row.count(0) for row in arr)

        # 종료 조건
        if cnt >= K:
            return cnt


N, K = map(int, input().split())
data = list(map(int, input().split()))
arr = [data[:N], data[N:]]
result = conveyor(N, K, arr)
print(result)
