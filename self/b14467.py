'''
소 1~10번
위치: 길의 왼쪽0 오른쪽1
'''
N = int(input())
observed = [None] * 11
cnt = 0

for _ in range(N):
    C, L = map(int, input().split())
    
    if observed[C] is None:  # 소를 처음 관찰 -> 위치 저장
        observed[C] = L
    elif observed[C] != L:  # 위치 바뀌었다면
        cnt += 1
        observed[C] = L  # 새로운 위치로 갱신

print(cnt)
