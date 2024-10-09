'''
회전 초밥
- 같은 종류 둘 이상 있을 수 있음
1. 임의 위치부터 K개 접시를 연속해서 먹을 경우 할인된 가격
2. 초밥의 종류가 쓰인 쿠폰 발생, 1번 참가 -> 쿠폰에 적힌 초밥 하나 무료 제공
- 벨트에 없으면 새로 만들어 손님에게 제공

가능한 다양한 초밥 먹는 게 목적
'''
N, D, K, C = map(int, input().split())
susi = []
for _ in range(N):
    susi.append(int(input()))

candidate = []
# K개 = N-1 - () +1
# () = N-K
for i in range(N-K+1):
    candidate.append(susi[i:i+4])
# candidate = [[7, 9, 7, 30], [9, 7, 30, 2], [7, 30, 2, 7], [30, 2, 7, 9], [2, 7, 9, 25]]

# 몇 종류 가능한지
numbers = []

max_eat = 0
for lst in candidate:
    if C not in lst:
        eat = len(set(lst)) + 1
        max_eat = max(max_eat, eat)
    else:
        eat = len(set(lst))
        max_eat = max(max_eat, eat)
print(max_eat)