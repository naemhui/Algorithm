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

arr = [list(map(int, input().split())) for _ in range(3)]
print(arr)