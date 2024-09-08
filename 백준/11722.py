A = int(input())
sequence = list(map(int, input().split()))
dp = [1]*A
# dp[i]에 i까지 봤을 때 가장 긴 감소하는 부분수열의 길이 저장

for i in range(1, A):
    for j in range(i):
        if sequence[i] < sequence[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))