# [r1, c1, r2, c2]
# 시작 위치: (r1, c2)



# def area(r1, c1, r2, c2):
#     arr = [[0]*100 for _ in range(100)]
#     for r in range(r1, r2+1):
#         for c in range(c1, c2+1):
#             if arr[r][c] == 0:
#                 arr[r][c] += 1
#             else:
#                 pass



# for _ in range(4):
#     r1, c1, r2, c2 = map(int, input().split())
#     area(r1, c1, r2, c2)







######################
arr = [[0]*100 for _ in range(100)]
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            arr[r][c] += 1
            if arr[r][c] == 0:
                arr[r][c] += 1
            else:
                pass
print(arr)
# count = 0
# for r in range(100):
#     for c in range(100):
#         if arr[r][c] != 0:
#             count += 1
# print(count)
# area(1, 2, 4, 4)
# area(2, 3, 5, 7)
# area(3, 1, 6, 5)
# area(7, 3, 8, 6)


