K = int(input())
for _ in range(K):
    n, s, d = map(int, input().split())
    ans = 0

    for i in range(n):
        di, vi = map(int, input().split())
        if d*s >= di:
            ans = ans + vi
    
    print(f'Data Set {_+1}:')
    print(ans)
    print()