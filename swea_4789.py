# 성공적이 공연 기획

# 문자열
# idx : 0 1 2 3 4 5
# cnt : 1 1 0 0 1 1

# 1: 기립 박수를 하고 있는 사람이 0명 이상일 때 1명
# 1: 기립 박수를 하고 있는 사람이 1명 이상일 때 1명
# 0: 기립 박수를 하고 있는 사람이 2명 이상일 때 0명
# 0 : 기립 박수를 하고 있는 사람이 3명 이상일 때 0명
# 1: 기립 박수를 하고 있는 사람이 4명 이상일 때 1명
# 1 : 기립 박수를 하고 있는 사람이 5명 이상일 때 1명이 기립박수를 한다.

# 즉, 0명만 있어도 2명은 박수를 치고, 2명이 더 있어야 나머지 2명도 침 -> 2명 고용
# people = 0  # cnt 가 N이 되어야 종료

def clap(lst):
    people = 0
    clapping = 0

    for i in range(len(lst)):
        if clapping < i:
            people += i - clapping
            clapping = i

        clapping += lst[i]
    
    return people


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    result = clap(lst)
    print(f'#{tc} {result}')


# clap(사람 별 clap, 사람 수)
# def clap(lst, N):
#     people = 0
#     i = 0
#     cnt = 0

#     while people < N:
#         if lst[i]:  # lst[i]가 0이 아닐 경우
#             people += lst[i]
#             i += lst[i]
#             # for j in range(i, i+people):
#             if people == N:
#                 return cnt
#         else:  # lst[i]가 0일 경우
#             i += 1
#             cnt += 1


# T = int(input())
# for tc in range(1, T+1):
#     lst = list(map(int, input()))
#     result = clap(lst, sum(lst))
#     print(f'#{tc} {result}')
