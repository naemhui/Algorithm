'''
1. 순열 만들기
2. 중복 - 한 자릿수 중에 겹치거나 두 자릿수 중에 겹치거나
3. ex. 1, 2, 12 들어오면 어쩌라고
'''
# 입력 받기
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

visited = [False] * n
result = set()  # 중복 제거된 정수들을 저장할 set

# 순열을 만들기 위한 DFS 함수
def dfs(level, now_num):
    if level == k:
        result.add(now_num)  # 중복 없이 숫자를 저장
        return

    for i in range(n):
        if not visited[i]:  # 아직 사용하지 않은 카드라면
            visited[i] = True
            dfs(level + 1, now_num + cards[i])  # 카드를 이어붙임
            visited[i] = False  # 방문 기록을 되돌림

dfs(0, "")

# 결과 출력
print(len(result))
