# cnt = 0
# for i in range(2, 2):
#     print(cnt+i)
# lst = list(map(int, input()))
# print(lst)

# lst = [1,0, 2, 3]
# if lst[1]:
#     print('i')

# a = list(map(str, input()))
# # print(type(a))
# print(a)
# print(a[:2])
# i = 2
# a[i:] = ['1']*(len(a)-2)
# print(a)

# T = int(input())
# for tc in range(1, T+1):
#     memory = list(map(str, input()))
#     print([0]*len(memory), memory)

# switch = [0, 1, 1, 1, 0, 0, 0, 1, 1]
# S = 9
# N = 3
# G = 1
# if G == 1:
#     for s in range(N-1, S, N):
#         if switch[s] == 0:
#             switch[s] = 1
#         else:
#             switch[s] = 0
# print(switch)
# C = 2
# R = 4
# arr = list([0]*C for _ in range(R))
# print(arr)

# arr = [['A','B','C','D','E'] for _ in range(5)]
# for j in range(5):
#     for i in range(5):
#         print(arr[i][j], end=" ")

# while cnt < N:
#     d = days % 7
#     if day[d] == 1:
#         cnt += 1
#         days += 1
#         if cnt >= N:
#             print(f'#{tc} {days - no}')
#             break