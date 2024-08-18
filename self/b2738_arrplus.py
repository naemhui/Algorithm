'''
N*M 행렬
행렬의 합 출력
'''

N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        arr[r][c] += arr1[r][c] + arr2[r][c]

for r in range(N):
    print(*arr[r])