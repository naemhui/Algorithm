<<<<<<< HEAD
# arr = [list(map(int, input().split())) for _ in range(9)]

# max_v = 0
# for r in range(9):
#     for c in range(9):
#         if arr[r][c] > max_v:
#             max_v = arr[r][c]
#             nr, nc = r+1, c+1
# print(max_v)
# print(nr, nc)

arr = [list(map(int, input().split())) for _ in range(9)]

max_v = 0
mr, mc = 0, 0
for r in range(9):
    for c in range(9):
        if max_v < arr[r][c]:
            mr, mc = r+1, c+1
            max_v = arr[r][c]

print(max_v)
=======
# arr = [list(map(int, input().split())) for _ in range(9)]

# max_v = 0
# for r in range(9):
#     for c in range(9):
#         if arr[r][c] > max_v:
#             max_v = arr[r][c]
#             nr, nc = r+1, c+1
# print(max_v)
# print(nr, nc)

arr = [list(map(int, input().split())) for _ in range(9)]

max_v = 0
mr, mc = 0, 0
for r in range(9):
    for c in range(9):
        if max_v < arr[r][c]:
            mr, mc = r+1, c+1
            max_v = arr[r][c]

print(max_v)
>>>>>>> 6359f9d65740511ff3257821461c2814158000e1
print(mr, mc)