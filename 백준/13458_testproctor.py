'''
N개의 시험장, i번 시험장 응시자 수: Ai
총감독관: B / 부감독관: C 응시자 감시 가능
각 시험장에 총감독관은 딱 1명
'''
N = int(input())
A_lst = list(map(int, input().split()))
B, C = map(int, input().split())  # 총감독, 부감독 각각 감시 가능한 수

g_cnt = len(A_lst)  # 필요한 총감독 수
d_cnt = 0  # 필요한 부감독 수

for i in range(len(A_lst)):

    # 총감독관 배정
    if A_lst[i] >= B:
        A_lst[i] -= B
    elif A_lst[i] < B:
        A_lst[i] = 0

    # 부감독관이 얼마나 더 필요한가
    d_cnt += A_lst[i]//C
    if A_lst[i] % C > 0:
        d_cnt += 1

print(g_cnt + d_cnt)