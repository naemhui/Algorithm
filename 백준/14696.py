# 별 > 동그라미 > 네모 > 세모 > 무승부
#  4      3        2      1

def winner(a, b, shape):
    # 종료 조건
    if shape == 0:  # 4321 검사 후에도 함수 종료가 안 됐다면
        print('D')  # 무승부인 거임
        return

    s = str(shape)
    a_cnt = a.count(s)
    b_cnt = b.count(s)
    
    if a_cnt > b_cnt:
        print('A')
        return
    elif a_cnt < b_cnt:
        # return 'B'
        print('B')
        return
    else:
        winner(a, b, shape-1)  # 재귀 호출


N = int(input())
for _ in range(N):
    a = input().split()
    b = input().split()
    winner(a[1:], b[1:], 4)  # 첫 번째 숫자 필요X