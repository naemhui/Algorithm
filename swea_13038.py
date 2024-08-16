'''
인덱스:  0 1 2  3  4 5  6
요일 : 일 월 화 수 목 금 토
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    day = list(map(int, input().split()))

    min_days = float('inf')

    for start in range(7):
        # 수업이 있는 요일에서 모두 각각 탐색!!!
        if day[start] == 1:
            cnt = 0
            days = 0
            now = start

            while cnt < N:
                if day[now % 7] == 1:
                    cnt += 1
                now += 1
                days += 1

            min_days = min(min_days, days)

    print(f'#{tc} {min_days}')


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     day = list(map(int, input().split()))

#     cnt = 0  # 수업 들은 날 카운트, N이랑 같아지면 프린트
#     days = 0  # 지난 날짜
#     no = day.index(1)

#     while cnt < N:
#         d = days % 7
#         if day[d] == 1:
#             cnt += 1
#             days += 1
#             if cnt >= N:
#                 print(f'#{tc} {days - no}')
#                 break
#         elif day[d] == 0:
#             days += 1