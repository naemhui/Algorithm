def onof(number):
    if number == 0:
        # number = 1
        return 1
    else:
        # number = 0
        return 0

S = int(input())  # 스위치 개수
switch = list(map(int, input().split()))
T = int(input())  # 학생 수

for _ in range(T):
    G, N = map(int, input().split())


    # 남자
    if G == 1:
        for s in range(N-1, S, N):
            switch[s] = onof(switch[s])

    # 여자
    else:
        # 스위치의 인덱스가 0 또는 S-1일 경우
        if N == 1 or N == S:  
            switch[N-1] = onof(switch[N-1])

        # 좌우 대칭 아닐 경우
        elif switch[N-2] != switch[N]:  
            switch[N-1] = onof(switch[N-1])

        # for s in range(1, S):
        else:
            if S - N >= N:  # N이 왼쪽에 있는 경우
                for i in range(N-2, -1, -1):
                    if switch[i] == switch[2*N-2-i]:
                        
            else:
                for i in range(N, S):
                    if switch[i] == switch[N-1 - (i-(N-2))]:
                        
            onof(switch[N-1])
N-1-i+N-1