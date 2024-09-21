'''
W를 이루고 있는 g개의 그림문자, 마야 문자열 S
-> W가 S에 들어있을 수 있는 모든 가짓수
즉, S 안에 W의 순열 중 하나가 부분 문자열로 들어있는 경우의 수

g(W의 길이) |S|(S의 길이)
W
S
'''
g, s = map(int, input().split())
W = input().strip()
S = input().strip()


visited = [False]*g
results = set()

def dfs(level, now_alp):
    if level == g:
        results.add(now_alp)
        return
    
    for i in range(g):
        if not visited[i]:
            visited[i] = True
            dfs(level+1, now_alp + W[i])
            visited[i] = False
dfs(0,'')

cnt = 0
for i in range(s-g+1):
    word = S[i:i+g]
    if word in results:
        cnt += 1

print(cnt)