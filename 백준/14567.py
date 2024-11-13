from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

answer = [1] *(N+1)  # 정답 입력될 리스트

def topology_sort():
    result = []  # 위상정렬 된 리스트
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = 1

    for i in range(1, N+1):
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
            answer[next] = answer[now] + 1
    print(*answer[1:])

topology_sort()