while 1:
    try:
        n, k = map(int, input().split())
        ans = 0
        ans += n
        while n // k:
            ans += n//k
            n = n//k + n%k
        print(ans)
    except EOFError:
        break