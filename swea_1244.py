# def onof(number):
#     if number == 0:
#         # number = 1
#         return 1
#     else:
#         # number = 0
#         return 0

def onof(number):
    return 1 if number == 0 else 0

S = int(input())  # 스위치 개수
switch = list(map(int, input().split()))
T = int(input())  # 학생 수

for _ in range(T):
    G, N = map(int, input().split())


    # 남자
    if G == 1:
        for i in range(N-1, S, N):
            switch[i] = onof(switch[i])

    # 여자
    elif G == 2:
        N -= 1  # 인덱스 맞추기 위해 !!
        switch[N] = onof(switch[N])

        # 좌우 대칭 확인
        left, right = N-1, N+1
        while left>=0 and right<S and switch[left] == switch[right]:
            switch[left] = onof(switch[left])
            switch[right] = onof(switch[right])
            left -= 1
            right += 1

    # # 여자
    # else:
    #     # 스위치의 인덱스가 0 또는 S-1일 경우
    #     if N == 1 or N == S:  
    #         switch[N-1] = onof(switch[N-1])

    #     # 좌우 대칭 아닐 경우
    #     elif switch[N-2] != switch[N]:  
    #         switch[N-1] = onof(switch[N-1])

    #     # for s in range(1, S):
    #     else:
    #         switch[N-1] = onof(switch[N-1])  # 일단 자기 자신 바꾸고

    #         # N이 왼쪽에 있는 경우
    #         if S - N >= N:
    #             for i in range(N-2, -1, -1):  # 나머지 구간 찾아서 바꿈
    #                 if switch[i] == switch[2*N-2-i]:
    #                     switch[i] = onof(switch[i])
    #                     switch[2*N-2-i] = onof(switch[2*N-2-i])
    #                 else:
    #                     break

    #         # N이 오른쪽에 있는 경우
    #         else:
    #             for i in range(N, S):
    #                 if switch[i] == switch[N-1 - (i-(N-2))]:
    #                     switch[i] = onof(switch[i])
    #                     switch[2*N-2-i] = onof(switch[2*N-2-i])
    #                 else:
    #                     break
for i in range(0, S, 20):
    print(*switch[i:i+20])