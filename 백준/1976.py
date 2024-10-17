from collections import deque

N = int(input())  # 도시들의 수
M = int(input())  # 여행 계획에 속한 도시들의 수

lst = [list(map(int, input().split())) for _ in range(N)]
travel = list(map(int, input().split()))  # 여행 계획
visited = [0]*N

start = travel[0]-1
check = True  # 여행 가능 여부


def bfs():
    # global start
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        naem = q.popleft()

        for i, item in enumerate(lst[naem]):
            # print(i, lst[naem])
            if visited[i] == 0 and item:
                visited[i] = 1
                q.append(i)
bfs()

for city in travel:
    if visited[city-1] == 0:
        check = False
if check:
    print("YES")
else:
    print("NO")

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i, item in enumerate(arr):
#     print(i, item)