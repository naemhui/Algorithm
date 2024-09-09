'''
N, M이 주어졌을 때, 만족하는 길이가 M인 수열을 모두 구하는 프로그램
- 1부터 N까지 자연수 중 중복 없이 M개를 고른 수열
'''
def dfs():
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        sequence.append(i)
        dfs()
        sequence.pop()
        # print(sequence)
        # print(visited)
        visited[i] = 0

N, M = map(int, input().split())
sequence = []
visited = [0] * (N+1)

dfs()