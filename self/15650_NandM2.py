'''
1~N까지 자연수 중 중복 없이 M개를 고른 수열
'''

def dfs(idx):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(idx, N+1):
        if visited[i]:
            continue
        
        sequence.append(i)
        visited[i] = 1
        dfs(i)
        sequence.pop()
        visited[i] = 0

N, M = map(int, input().split())
sequence = []
visited = [0]*(N+1)

dfs(1)