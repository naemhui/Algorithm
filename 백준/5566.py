N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
now = 1
cnt = 0
for _ in range(M):
    # now += int(input())
    dice = int(input())
    now += dice

    if now >= N:
        cnt += 1
        break

    now += board[now-1]
    cnt += 1

    if now >= N:
        break

print(cnt)