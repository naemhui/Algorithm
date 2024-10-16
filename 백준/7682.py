# while 1:
#     if input() == "end":
#         break
#     board = []

# 특정 플레이어(t, 즉 'X' 또는 'O')가 승리했는지 여부를 확인하는 함수
def tickto(arr, t):

    # 가로, 세로, 대각선 검사(3칸 잇는 경우)
    if t == arr[0] == arr[1] == arr[2]:
        return True
    if t == arr[3] ==arr[4] ==arr[5]:
        return True
    if t == arr[6] == arr[7] == arr[8]:
        return True
    if t ==arr[0] == arr[4] ==arr[8]:
        return True
    if t == arr[2] == arr[4] == arr[6]:
        return True
    if t == arr[0] == arr[3] == arr[6]:
        return True
    if t == arr[1] == arr[4] == arr[7]:
        return True
    if t == arr[2] == arr[5] == arr[8]:
        return True

    return False

while True:
    a = input()
    if a == "end":
        break
    else:
        flag = True
        arr = list(map(str, a))
        xcnt = arr.count('X')
        ocnt = arr.count('O')

        # 조건1. X가 O보다 1개 많거나, X와 O의 개수가 같아야 함
        if xcnt > ocnt+1:
            print("invalid")
            continue

        # 조건 2. O의 개수가 X의 개수와 같을 때
        # O와 X의 개수가 같을 때는 O가 이겼을 경우만 유효한 게임 상태
        # O가 이겼고, X는 이기지 않았을 때만 "valid"를 출력
        if ocnt == xcnt :
            if tickto(arr,'O') and not tickto(arr, 'X'):
                print("valid")
                continue

        # 조건 3. O의 개수가 X보다 많을 때
        if ocnt >xcnt :
            print("invalid")
            continue

        # 조건 4. X가 O보다 1개 많을 때
        # X가 O보다 1개 더 많을 때는 X가 이겼을 경우만 유효한 상태
        # X가 이기고, O는 이기지 않았을 경우 "valid"를 출력
        if ocnt +1 == xcnt :
            if tickto(arr,'X') and not tickto(arr,'O'):
                print("valid")
                continue

        # 조건 5. 게임판이 가득 찬 경우
        # O가 이기지 않았다면 유효한 상태 -> X가 승리 or 무승부
        if xcnt == 5 and ocnt ==4:
            if not tickto(arr, "O"):
                print("valid")
                continue

        # 위 조건들 모두 통과하지 못하면 게임판 유효하지 않음
        print("invalid")