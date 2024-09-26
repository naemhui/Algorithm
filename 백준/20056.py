dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

def move():
    new_fireballs = []
    arr = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        arr[nr][nc].append([m, s, d])
    
    return arr

def split(arr):
    new_fireballs = []
    
    for r in range(N):
        for c in range(N):
            # print('arr', arr)
            # print('arr[r][c]', arr[r][c])
            if len(arr[r][c]) == 1:
                new_fireballs.append([r, c] + arr[r][c][0])
                # print(arr[r][c], arr[r][c][0])

            elif len(arr[r][c]) > 1:
                # print(arr[r][c], arr[r][c][0])
                mass = speed = cnt = 0
                is_odd = is_even = True
                
                for m, s, d in arr[r][c]:
                    mass += m
                    speed += s
                    cnt += 1
                    if d % 2 == 0:
                        is_odd = False
                    else:
                        is_even = False
                
                new_m = mass // 5
                new_s = speed // cnt
                
                if new_m > 0:
                    if is_odd or is_even:
                        directions = [0, 2, 4, 6]
                    else:
                        directions = [1, 3, 5, 7]
                    
                    for d in directions:
                        new_fireballs.append([r, c, new_m, new_s, d])
                # print(arr[r][c], arr[r][c][0])
    
    return new_fireballs

for _ in range(K):
    arr = move()
    fireballs = split(arr)
# print(fireballs)

total = 0
for _ in range(len(fireballs)):
    total += fireballs[_][2]
print(total)