arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
bingo = [[0]*5 for _ in range(5)]


def bingo_check(bingo):
    clear = 0
    # 가로 빙고 확인
    for r in bingo:
        if sum(r) == 5:
            clear += 1

    # 세로 빙고 확인
    for c in range(5):
        sum_c = 0
        for r in range(5):
            sum_c += bingo[r][c]
        if sum_c == 5:
            clear += 1

    # 대각선 빙고 확인
    sum_d1 = 0
    for r in range(5):
        sum_d1 += bingo[r][r]
    if sum_d1 == 5:
        clear += 1
    
    # 대각선 빙고 확인2
    sum_d2 = 0
    for r in range(5):
        sum_d2 += bingo[r][4-r]
    if sum_d2 == 5:
        clear += 1

    return clear


cnt = 0
clear = 0

for i in range(5):
    for j in range(5):
        num = arr2[i][j]  # 사회자가 부른 num
        cnt += 1

        for k in range(5):    
            if num in arr1[k]:  # num 인덱스 저장
                idx = arr1[k].index(num)
                bingo[k][idx] = 1
                break  # 숫자 안 겹치니까 찾으면 바로 break

        clear = bingo_check(bingo)
        if clear >= 3:
            print(cnt)
            exit()