'''
회전 초밥
- 같은 종류 둘 이상 있을 수 있음
1. 임의 위치부터 K개 접시를 연속해서 먹을 경우 할인된 가격
2. 초밥의 종류가 쓰인 쿠폰 발생, 1번 참가 -> 쿠폰에 적힌 초밥 하나 무료 제공
- 벨트에 없으면 새로 만들어 손님에게 제공

가능한 다양한 초밥 먹는 게 목적
'''
N, D, K, C = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

sushi += sushi[:K-1]
# print(susi)

# K개 = N-1 - () +1
# () = N-K

sum_v = max_sum = 0

for i in range(N):
    candidate = sushi[i:i+K]
    # print(i, candidate)
    if C not in candidate:
        sum_v = len(set(candidate)) + 1
        max_sum = max(max_sum, sum_v)
    else:
        sum_v = len(set(candidate))
        max_sum = max(max_sum, sum_v)
print(max_sum)