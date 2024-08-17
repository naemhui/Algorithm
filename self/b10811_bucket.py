N, M = map(int, input().split())
bucket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    # for k in range(i-1, j):
    # for a in range(j-1, i, -1):
    bucket[i-1:j] = bucket[i-1:j][::-1]

print(*bucket)