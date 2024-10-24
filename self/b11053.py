N = int(input())
num = list(map(int, input().split()))

dp = [1] * N  # LIS 저장하는 배열 (dp[i] = i번째 수를 끝으로 하는 LIS 길이)

# 가장 긴 증가하는 수열 찾기 
for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)
# 여기까지 했을 때 d 배열에는 각 인덱스에서 끝나는 최장 증가 부분 수열의 길이가 저장됨

print(max(dp))