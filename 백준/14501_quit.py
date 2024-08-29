def max_profit(N, T, P):
    # DP 배열 초기화: dp[i]는 i일부터 시작했을 때 얻을 수 있는 최대 수익
    dp = [0] * (N + 1)
    
    # 마지막 날부터 첫째 날까지 역순으로 계산
    for i in range(N - 1, -1, -1):
        if i + T[i] > N:
            # 상담이 퇴사일을 넘어가는 경우
            dp[i] = dp[i + 1]
        else:
            # 현재 상담을 하는 경우와 하지 않는 경우 중 최대값 선택
            dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    
    return dp[0]

# 입력 읽기
N = int(input())
T = []
P = []

for _ in range(N):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

print(max_profit(N, T, P))
