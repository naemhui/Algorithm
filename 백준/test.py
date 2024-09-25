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

# arr1 = [list(map(int, input().split())) for _ in range(5)]
# arr2 = [list(map(int, input().split())) for _ in range(5)]
# bingo = [[0]*5 for _ in range(5)]

# clear = 0
# def bingo_check(bingo, i, j):

#     # 가로 빙고 확인
#     for r in bingo:
#         if sum(r) == 5:
#             clear += 1

#     # 세로 빙고 확인
#     for c in range(5):
#         sum_c = 0
#         for r in range(5):
#             sum_c += bingo[r][c]
#         if sum_c == 5:
#             clear += 1

#     # 대각선 빙고 확인
#     sum_d1 = 0
#     for r in range(5):
#         sum_d1 += bingo[r][r]
#     if sum_d1 == 5:
#         clear += 1
    
#     # 대각선 빙고 확인2
#     sum_d2 = 0
#     for r in range(5):
#         sum_d2 += bingo[r][4-r]
#     if sum_d2 == 5:
#         clear += 1

#     return clear


# cnt = 0

# for i in range(5):
#     for j in range(5):
#         num = arr2[i][j]  # 사회자가 부른 num
#         cnt += 1

#         for k in range(5):    
#             if num in arr1[k]:  # num 인덱스 저장
#                 idx = arr1[k].index(num)
#                 bingo[k][idx] = 1

#         clear = bingo_check(bingo, i, j)
#         if clear == 3:
#             print(cnt)
            


# ####### snake
# '''
# N*N 정사각 보드
# 사과 -> 뱀 길이 늘어남
# 벽, 자기 몸 -> 게임 끝
# '''
# def is_valid(r,c,N):
#     return 0<=r<N and 0<=c<N


# # 뱀 이동 함수
# def snake(r,c,N,arr):
    


# # 우 하 좌 상 (반시계방향)
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# N = int(input())  # 보드 크기
# arr = [[0]*N for _ in range(N)]
# K = int(input())  # 사과 개수
# for _ in range(K):
#     r, c = map(int, input().split())  # 사과의 위치
#     arr[r-1][c-1] = 1  # 사과 위치에 1 표시

# L = int(input())  # 방향 변환 횟수

# d = 0  # 시작 방향(우)
# i, j = 0, 0
# for _ in range(L):
#     X, C = input().split()  # x초 후 왼(L) 또는 오(D)로 90도 회전
#     for x in range(X):
#         i += d[dr]
#         j += d[dc]
#         if is_valid(ni,nj,N):
#             pass
    
#     if c == D:
#         d += 1
#         ni = i + d[dr]
#         nj = j + d[dc]

# a = 'dz==dz='
# print(a.count('dz='))

# arr = [[0]*2 for _ in range(3)]
# print(arr)

# command = list(map(int, input().split()))
# for i in range(len(command)):
#     command[i] -= 1
# print(command)
# arr = ['A', 'B', 'C', 'D', 'E'] # 이중 3개 중복 없이 뽑기
# path = []
# n = 3


# def run(lev, start):
#     if lev == n:
#         print(path[0])
#         # print(path)
#         return

#     for i in range(start, 5):
#         path.append(arr[i])
#         run(lev + 1, i + 1)  # i 업데이트 -> 중복X
#         path.pop()

# run(0, 0)

# def navi(i, j, hole_i, hole_j):
#     # 2사분면
#     if i < hole_i and j < hole_j:


#     # 1사분면
#     elif i < hole_i and j > hole_j:

    
#     # 3사분면
#     elif i > hole_i and j < hole_j:

    
#     # 4사분면
#     else:

# arr = [3, 5, 7, 2, 1, 0]
# arr = qsort(arr)

# def qsort(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[0][0]  # 첫 번째 요소의 나이 (정렬 기준)
#     low = []
#     high = []
#     for i in range(1, len(arr)):
#         value = arr[i][0]  # 배열의 나이를 기준으로 비교
#         if value < pivot:
#             low.append(arr[i])
#         else:
#             high.append(arr[i])

#     return qsort(low) + [arr[0]] + qsort(high)  # arr[0]을 기준점으로 추가


# N = int(input())
# arr = []
# for _ in range(N):
#     age, name = input().split()
#     age = int(age)
#     arr.append([age, name])

# print(qsort(arr))

# 순열

# arr = [1, 1, 2, 3, 4]
# visited = [False] * len(arr)
# result = [0] * len(arr)

# def dfs(level):
#     if level == len(arr):
#         print(*result)
#         return

#     for i in range(len(arr)):
#         # 가지치기 : 중복된 숫자 제거
#         if visited[i]:
#             continue

#         visited[i] = True
#         result[level] = arr[i]
#         dfs(level + 1)
#         visited[i] = False

# # dfs(0)

# arr = [1, 1, 2, 3, 4]
# arr.sort()  # 배열을 정렬하여 중복된 숫자를 연속적으로 배치
# visited = [False] * len(arr)
# result = [0] * len(arr)

# def dfs(level):
#     if level == len(arr):
#         print(*result)
#         return

#     last_used = None  # 같은 레벨에서 마지막으로 사용된 숫자를 기록
#     for i in range(len(arr)):
#         # 가지치기: 이미 방문한 숫자 또는 같은 레벨에서 이미 사용된 숫자 건너뛰기
#         if visited[i] or arr[i] == last_used:
#             continue

#         visited[i] = True
#         result[level] = arr[i]
#         last_used = arr[i]  # 이번 레벨에서 사용된 숫자를 기록
#         dfs(level + 1)
#         visited[i] = False

# dfs(0)

# print(-7%4)
# print(7%4)\
# N = 5
# arr = [[0]*(N+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     arr[i][1:N+1] = map(int, input().split())

# print(arr)
N = 3
idxs = [list(range(N)), list(range(N-1,-1,-1))]
# print(idxs)
# [0, N-2, N-1, N-1, N-2, 0]
# [0, N-2, N-1, N, N+1, N+2]
# N = 4
# arr = [[0]*8]+[list(map(int,input())) for _ in range(N)]
# print(arr)
# cogwheel = [1, 2, 3, 4]
# print(cogwheel.index(2))
# print(cogwheel.pop(2))
# print(cogwheel)

# clockwise = [-1, 0]*10
# print(clockwise)
# arr = [1, 2, 3, 4, 5, 6]
# # arr = [arr[-1]] + arr[:-1]
# # print(arr)
# arr = [1, 2, 3, 4, 5, 6]
# # arr= arr[1:] + [arr[0]]
# # print(arr)
# for i in range(5, 5):
#     print(i)

# # 톱니바퀴 배열 입력 받기
# arr = [list(map(int, input().strip())) for _ in range(4)]
# K = int(input())  # 회전 횟수 입력
# commands = [list(map(int, input().split())) for _ in range(K)]  # 회전 명령 입력

# # 톱니바퀴 회전 함수
# def rotate(cog, direction):
#     if direction == 1:  # 시계 방향
#         arr[cog] = [arr[cog][-1]] + arr[cog][:-1]
#     else:  # 반시계 방향
#         arr[cog] = arr[cog][1:] + [arr[cog][0]]

# # 회전 명령 처리
# for N, D in commands:
#     N -= 1  # 인덱스 맞춤 (1번 톱니바퀴는 arr[0]에 해당)
#     rotations = [0] * 4  # 각 톱니바퀴의 회전 방향 저장
#     rotations[N] = D  # 회전하려는 톱니바퀴의 회전 방향 설정
    
#     # 왼쪽 톱니바퀴 회전 여부 확인
#     for i in range(N-1, -1, -1):
#         if arr[i][2] != arr[i+1][6]:  # 극이 다르면
#             rotations[i] = -rotations[i+1]
#         else:
#             break

#     # 오른쪽 톱니바퀴 회전 여부 확인
#     for i in range(N+1, 4):
#         if arr[i-1][2] != arr[i][6]:  # 극이 다르면
#             rotations[i] = -rotations[i-1]
#         else:
#             break

#     # 각 톱니바퀴 회전
#     for i in range(4):
#         if rotations[i] != 0:
#             rotate(i, rotations[i])

# # 점수 계산
# score = 0
# if arr[0][0] == 1:
#     score += 1
# if arr[1][0] == 1:
#     score += 2
# if arr[2][0] == 1:
#     score += 4
# if arr[3][0] == 1:
#     score += 8

# # 결과 출력
# print(score)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(arr[:-1])
# print(arr[::-1])
print(arr[1:6])