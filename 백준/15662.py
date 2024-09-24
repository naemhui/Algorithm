T = int(input())
arr = [list(map(int, input().strip())) for _ in range(T)]
K = int(input())
commands = [list(map(int, input().split())) for _ in range(K)]


def rotate(cog, direction):
    if direction == 1:  # 시계 방향이면
        arr[cog] = [arr[cog][-1]] + arr[cog][:-1]
    else:  # 반시계 방향
        arr[cog] = arr[cog][1:] + [arr[cog][0]]


for N, D in commands:
    N -= 1  # 인덱스 맞춤
    rotations = [0] * T  # 톱니바퀴의 회전 방향
    rotations[N] = D  # 회전하려는 톱니바퀴의 회전 방향 설정할 것~
    
    # 왼쪽 톱니바퀴부터 확인
    for i in range(N-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:  # 극이 다르면
            rotations[i] = -rotations[i+1]
        else:
            break
    
    # 오른쪽 톱니바퀴 확인
    for i in range(N+1, T):
        if arr[i-1][2] != arr[i][6]:  # 극이 다르면
            rotations[i] = -rotations[i-1]
        else:
            break
    
    for i in range(T):
        if rotations[i] != 0:
            rotate(i, rotations[i])


result = 0
for i in range(T):
    if arr[i][0] == 1:
        result += 1
print(result)