def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# def fibonacci(n):
#     dp = [0] * (n+1)
#     dp[1] = dp[2] = 1

#     cnt = 0

#     for i in range(3, n+1):
#        dp[i] = dp[i-1] + dp[i-2]
#     return cnt

def fibonacci(n):
   return n-2


N = int(input())
print(fib(N), fibonacci(N))