N = int(input())  # 남은 일 수
consult = [list(map(int, input().split())) for _ in range(N)]  # 상담 목록
dp = [0] * (N + 1)  # dp 배열 초기화 (N+1 크기)

# i일을 기준으로 반복
for i in range(N):
    Ti, Pi = consult[i]  # 상담 기간과 수익
    # 현재까지의 최대 수익을 다음 날로 넘김
    if i + 1 <= N:
        dp[i + 1] = max(dp[i + 1], dp[i])
    # 상담이 끝나는 날이 N일 이하일 때
    if i + Ti <= N:
        dp[i + Ti] = max(dp[i + Ti], dp[i] + Pi)

# 마지막 날까지 얻을 수 있는 최대 수익 출력
print(dp[N])