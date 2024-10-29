import sys
input = sys.stdin.readline

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])  # 경로 압축!
    return parents[x]

# a, b가 속한 집합 합치기 - 진실을 아는 사람이 부모
def union(a, b, truth):
    root_a = find(a)
    root_b = find(b)

    if root_a in truth and root_b in truth:
        return

    if root_a in truth:
        parents[root_b] = root_a
    elif root_b in truth:
        parents[root_a] = root_b
    else:
        if root_a < root_b:
            parents[root_b] = root_a
        else:
            parents[root_a] = root_b

N, M = map(int, input().split())
truth = set(map(int, input().split()[1:]))

party_members = []
parents = list(range(N + 1))

for _ in range(M):
    data = list(map(int, input().split()))
    party_size, members = data[0], data[1:]

    # 모든 멤버를 하나의 그룹으로 묶기
    for j in range(party_size - 1):
        union(members[j], members[j + 1], truth)
    
    party_members.append(members)

answer = 0
for members in party_members:
    # 파티에서 진실을 알고 있는 사람이 없을 때만 과장 가능
    for member in members:
        if find(member) in truth:
            break
    else:
        answer += 1

print(answer)