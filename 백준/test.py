# r = 9
# c = 9
# for r in range(99, 0, -1)
#     99 -= 1
#     if

# lst = [0, 1, 2, 3, 4]
# pop1 = lst.pop(0)
# print(lst)
# pop2 = lst.pop(1)
# print(lst)
# lst.insert(0, pop1)
# lst.insert(2, pop2)
# print(lst)

# for i in range(9):
#     lst = [int(input())]

# lst = [1, 2, 3, 4, 5]
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# data = [list(map(int, input().split())) for _ in range(2)]
# print(data)

# arr = [[0]*(10) for _ in range(10)]
# print(arr)

# data = [[2,2,4,4]]
# lst = []
# for i in range(len(data)):
#     for x in range(data[i][0], data[i][0] + data[i][2]):
#         for y in range(data[i][1], data[i][1] + data[i][3]):
#             lst.append([x, y])

# print(lst)

# lst = ['1', '2', '2']
# print(lst.count('3'))

# arr = list([0]*101 for _ in range(101))
# print(arr)

# arr = [[1, 1, 1],[0]]
# arr = [['1']]
# print(arr.count('1'))

# arr = [list(map(int, input().split())) for _ in range(3)]
# print(arr)

# seq = input().split()
# print(type(seq[1]))

# lst = [1, 2, 3, 4, 5, 6, 7]
# for i in range(0, 7, 4):
#     print(i)

# light = list(input())
# print(light)

# arr = [[1, 2, 3], [4, 5, 6]]
# # print(arr[0])
# a = arr[0]
# if a.index(2):
#     print('good')

arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
bingo = [[0]*5 for _ in range(5)]

clear = 0
def bingo_check(bingo, i, j):

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

for i in range(5):
    for j in range(5):
        num = arr2[i][j]  # 사회자가 부른 num
        cnt += 1

        for k in range(5):    
            if num in arr1[k]:  # num 인덱스 저장
                idx = arr1[k].index(num)
                bingo[k][idx] = 1

        clear = bingo_check(bingo, i, j)
        if clear == 3:
            print(cnt)
            