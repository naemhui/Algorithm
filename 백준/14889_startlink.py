N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')  # 두 팀간 능력치 차이의 최솟값
team = []  # 선택된 선수 인덱스


# 팀 능력치 계산
def calculate_ability(team):
    ability = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            ability += arr[team[i]][team[j]] + arr[team[j]][team[i]]
    return ability


# lev가 N // 2에 도달하면
# team을 스타트 팀으로, 나머지 사람들을 링크 팀으로 나누어 각각의 능력치를 계산
def run(lev, start):
    global min_diff
    if lev == N // 2:
        start_team = team
        link_team = [i for i in range(N) if i not in start_team]
        
        start_ability = calculate_ability(start_team)
        link_ability = calculate_ability(link_team)
        
        diff = abs(start_ability - link_ability)
        min_diff = min(min_diff, diff)
        return

    for i in range(start, N):
        team.append(i)
        run(lev + 1, i + 1)
        team.pop()

run(0, 0)
print(min_diff)