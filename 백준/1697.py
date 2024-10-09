'''
수빈: N, 동생: K
수빈 - 1초 후 1간 or 1초 후 2*X
'''
from collections import deque
N, K = map(int, input().split())

# 수빈 0 ~ 100000
max_v = 100000
visited = [0]*(max_v+1)

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        # 수빈 == 동생
        if x == K:
            return visited[x]

        for i in (x-1, x+1, 2*x):
            if 0<=i<=max_v and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

print(bfs())