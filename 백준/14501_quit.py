# 지정한 시작일로부터 돈 계산해주는 함수
def wage(N, start_day):
    global day
    global money
    global start

    if N >= day + T_lst[start_day]:
        day += T_lst[start_day]
        for i in range(start_day, T_lst[start_day]):
            money += P_lst[i]

    else:
        day = N
        for i in range(start_day, N):
            money += P_lst[i]

    # 아직 근무일 남아있으면 재귀 호출할게
    if N > day:
        wage(N, day)
    
    return money


N = int(input())  # 퇴사까지 남은 일수
T_lst = []
P_lst = []

for _ in range(N):
    T, P = map(int, input().split())
    T_lst.append(T)
    P_lst.append(P)

max_money = 0

for start in range(7):  # 각 날짜마다 시작해봄
    day = 0  # 며칠 일하는지
    money = 0  # 얼마 벌었는지
    result = wage(N, start)

    if result > max_money:
        max_money = result
print(max_money)