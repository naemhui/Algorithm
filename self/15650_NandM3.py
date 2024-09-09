N, M = map(int, input().split())
visited = [0]*(N+1)
sequence = []

def dfs():
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N+1):
        sequence.append(i)
        dfs()
        visited[i] = 1
        sequence.pop()

dfs()