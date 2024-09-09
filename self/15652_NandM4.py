N, M = map(int, input().split())
visited = [0]*(N+1)
sequence = []

def dfs(start):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N+1):
        sequence.append(i)
        dfs(i)
        sequence.pop()

dfs(1)