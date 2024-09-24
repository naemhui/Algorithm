'''
10101111
01111101
11001110
00000010

2(3번째)
6(7번째)
'''
# cogwheel = [0, 1, 2, 3, 4]
# plus = [-1, 1]*10
# minus = [1, -1]*10
# clock = True  # True면 시계 False면 반시계

arr = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
commands = [list(map(int, input().split())) for _ in range(K)]


def rotate(cog, direction):
    if direction == 1:  # 시계 방향이면
        arr[cog] = [arr[cog][-1]] + arr[cog][:-1]
    else:  # 반시계 방향
        arr[cog] = arr[cog][1:] + [arr[cog][0]]


for N, D in commands:
    N -= 1  # 인덱스 맞춤
    rotations = [0] * 4  # 톱니바퀴의 회전 방향
    rotations[N] = D  # 회전하려는 톱니바퀴의 회전 방향 설정할 것~
    
    # 왼쪽 톱니바퀴부터 확인
    for i in range(N-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:  # 극이 다르면
            rotations[i] = -rotations[i+1]
        else:
            break
    
    # 오른쪽 톱니바퀴 확인
    for i in range(N+1, 4):
        if arr[i-1][2] != arr[i][6]:  # 극이 다르면
            rotations[i] = -rotations[i-1]
        else:
            break
    
    for i in range(4):
        if rotations[i] != 0:
            rotate(i, rotations[i])


score = 0
if arr[0][0] == 1:
    score += 1
if arr[1][0] == 1:
    score += 2
if arr[2][0] == 1:
    score += 4
if arr[3][0] == 1:
    score += 8

print(score)