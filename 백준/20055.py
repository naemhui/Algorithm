def conveyor(arr):
    robot = [False]*(2*N)
    step = 0

    while True:
        step += 1

        # 컨베이어 벨트 회전
        arr = [arr[-1]] + arr[:-1]
        robot = [robot[-1]] + robot[:-1]
        robot[N-1] = False

        # 로봇 이동
        for i in range(N-2, -1, -1):
            # 로봇이 존재하고, 다음 칸에 로봇 없고, 내구도 있다면
            if robot[i] and not robot[i+1] and arr[i+1]>0:
                robot[i] = False
                robot[i+1] = True
                arr[i+1] -= 1

        robot[N-1] = False

        # 로봇 올리기
        if arr[0] > 0:
            robot[0] = True
            arr[0] -= 1

        # 내구도 0 개수 세기
        cnt = arr.count(0)
        if cnt >= K:
            return step
        
N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = conveyor(arr)
print(result)