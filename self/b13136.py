R, C, N = map(int, input().split())

if min(R, C) % N > 0:
    width = min(R, C) // N + 1
else:
    width = min(R, C) // N

if max(R, C) % N > 0:
    length = max(R, C) // N + 1
else:
    length = max(R, C) // N

print(width*length)