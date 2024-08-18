N = int(input())
arr = [[' ']*(2*N-1) for _ in range(2*N-1)]

# 가운데 : N//2
for i in range(2*N-1):
    # idx = abs(2*N//2-i)
    idx = abs(N-1-i)
    for j in range(idx, 2*N-1-idx):
        arr[i][j] = '*'

# for _ in arr:
#     print(*_)

for row in arr:
    print("".join(row).rstrip())