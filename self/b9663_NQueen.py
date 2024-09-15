n = int(input())
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # 같은 열에 있거나 / 같은 대각선 상에 있으면
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1  # 가능한 해결 방법의 수 기록하고 함수 종료
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i

            # 퀸들이 서로 공격하지 않으면
            if is_promising(x):
                # 재귀 호출(다음 행에 퀸을 놓기 위함)
                n_queens(x+1)

n_queens(0)
print(ans)