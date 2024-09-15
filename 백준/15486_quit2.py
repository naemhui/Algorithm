'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''

def counsel(arr):
    dp = [[0]*(N+1)]
    for s in range(1, N+1):
        for i in range(s):
            dp[s][i] = max(dp[s][i], dp[s-1][i] + arr[s][i])
            dp[s][i+1] = max(dp[s][i+1], dp[s-1][i] + arr[s][i+1])
    return max(dp[-1])

N = int(input())
arr = [[0]*(N+1) for _ in range(2)]
for _ in range(N):
    T, P = map(int, input().split())
    arr[0][_+1] = T
    arr[1][_+1] = P

counsel(arr)