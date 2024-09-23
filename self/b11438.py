import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
LENGTH = 21

n = int(input())
parent = [[0] * LENGTH for _ in range(n + 1)]
visited = [False] * (n + 1)
d = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        if visited[node]:
            continue
        # 우선 바로 위에 있는 부모 정보만 갱신
        parent[node][0] = x
        dfs(node, depth + 1)


# 모든 노드의 전체 부모 관계 갱신하기
def set_parent():
    dfs(1, 0)
    for i in range(1, LENGTH):
        for j in range(1, n + 1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(a, b):
    # 무조건 b의 깊이가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a

    # a와 b의 깊이가 동일해주도록 설정
    for i in range(LENGTH - 1, -1, -1):
        if d[b] - d[a] >= 2**i:
            b = parent[b][i]

    if a == b:
        return a

    # 올라가면서 공통 조상 찾기
    for i in range(LENGTH - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


set_parent()

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

######
# 다른 이해하기 쉬운 코드
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀 깊이 설정 
LOG = 21 # 2^20 = 1,000,000

n = int(input())
parent = [[0]*LOG for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드 깊이가 계산되었는지 여부 
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트노드부터 출발하여 깊이를 구하는 함수 
def dfs(x, depth):
    c[x] = True
    d[x] = depth

    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하기
def set_parent():
    dfs(1, 0) # 루트노드 1번부터 시작 
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상 찾기 
def lca(a, b):
    # B가 더 깊도록 설정 
    if d[a] > d[b]:
        a, b = b, a
    # 깊이가 동일하도록 
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
    	# 조상을 향해 거슬러 올라가기 
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 부모가 찾고자 하는 조상 
    return parent[a][0]


set_parent()
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

#####
# 또 다른 괜찮은 풀이
import sys
input = sys.stdin.readline
# 문제에서 주어진 최대 깊이를 기준으로
# 2분탐색으로 탐색하므로 log값 구하기
max_depth = 100000
LOG = 21
###########################################
n = int(input())

# 그래프 형태로 입력받기
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


###########################################
# 트리형태에서 부모노드와 자신의 레벨을 저장
tree = [[0 for _ in range(LOG)] for _ in range(n+1)]

visit = [1]
level = [-1 for _ in range(n+1)]
level[1] = 0

while visit:
    now = visit.pop()

    for next_node in graph[now]:
        if level[next_node] != -1:
            continue

        level[next_node] = level[now] + 1
        tree[next_node][0] = now
        visit.append(next_node)


###########################################
# 2진 형태의 조상 노드 구하기
for i in range(1, LOG):
    for j in range(1, n+1):
        tree[j][i] = tree[tree[j][i - 1]][i - 1]

# for i in tree:
#     print(i)
###########################################
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    # a의 레벨이 높도록 조절
    if level[a] < level[b]:
        a, b = b, a

    # 레벨 맞추기
    for i in range(LOG-1, -1, -1):
        if level[a] - level[b] >= 2 ** i:
            a = tree[a][i]

    if a == b:
        print(a)
        continue

    # 조상노드 찾기
    for i in range(LOG-1, -1, -1):
        if tree[a][i] != tree[b][i]:
            a = tree[a][i]
            b = tree[b][i]

    print(tree[a][0])