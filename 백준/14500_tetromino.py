'''
[1, 2, 2] -> [0, 0, -1] -> [0, 1, 2] -> [1, 0, 0]
[0, 0, 1] -> [1, 2, 2] -> [1, 1, 1] -> [0, 1, 2]
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

max_v = 0
# ㅗ 모양을 제외한 나머지 모양 탐색
def dfs(x, y, temp, cnt):
    global max_v
    if cnt == 4: # 탐색완료 후 최댓값 비교
        max_v = max(max_v, temp)
        return
    
    for i in range(4): # 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N or visited[ny][nx]:
            continue
        visited[ny][nx] = True # 방문처리
        dfs(nx, ny, temp+graph[ny][nx], cnt+1)
        visited[ny][nx] = False # 방문처리 제거

# ㅗ 모양 탐색
def dfs_T(x, y):
    global max_v
    temp = graph[y][x]
    arr = []
    
    for i in range(4): # 모든 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        arr.append(graph[ny][nx])
    length = len(arr)

    if length == 4 : # 만약 4방향 모두 nxm에 들어간다면 그중 가장 작은 값 제거 후 sum
        arr.sort(reverse=True)
        arr.pop()
        max_v = max(max_v, sum(arr) + graph[y][x])

    elif length == 3: # 3방향만 nxm에 들어가기 때문에 바로 sum
        max_v = max(max_v, sum(arr) + graph[y][x])

    return # length가 2 이하라면 ㅗ 모양이 아니므로 바로 return

for i in range(N):
    for j in range(M):
        visited[i][j] = True # 현재 지점 방문처리
        dfs(j, i, graph[i][j], 1)
        dfs_T(j, i)
        visited[i][j] = False

print(max_v) # 정답 출력