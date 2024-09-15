'''
사다리 조작
N*M (N이 열 M이 행)
H: 가로선을 놓을 수 있는 개수
사다리에 가로선을 추가 -> 결과 조작.
i번 세로선의 결과가  i번이 나와야 함
추가해야 하는 가로선 개수의 최솟값?

3보다 크거나 불가능한 경우 -1

그니까
사다리 그어보고 잘 도착하면 어찌구..ㅈㄴ어렵네미친
'''
N, M, H = map(int, input().split())
arr = [[0]*(N+1) for _ in range(M+1)]
cnt = []
visited = [[0] * (N+1) for _ in range(M+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1


def dfs():
    if len(cnt) == H:
        # print(cnt)
        return len(cnt)
    
    elif len(cnt) > H+1:
        # print(cnt)
        return -1
    
    
    for i in range(1, M+1):
        for j in range(1, N+1):
            if arr[i][j]:
                continue
            visited[i][j] = 1
            cnt.append([i, j])
            dfs()
            cnt.pop()
            visited[i][j] = 0

# print(dfs())
dfs()