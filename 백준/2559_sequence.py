# N, K = map(int, input().split())
# temp = list(map(int, input().split()))
# max_v = (-1)*10**7

# for i in range(N-K+1):
#     sum_v = 0
#     for j in range(i, i+K):
#         sum_v += temp[j]
#     if sum_v > max_v:
#         max_v = sum_v

# print(max_v)

N, K = map(int, input().split())
temp = list(map(int, input().split()))

# 첫 번째 구간의 합을 구함
sum_v = sum(temp[:K])
max_sum = sum_v

# 슬라이딩 윈도우를 사용하여 구간 합을 업데이트
for i in range(K, N):
    sum_v += temp[i] - temp[i - K]  # 새로운 요소를 더하고, 이전 요소를 뺌
    max_sum = max(max_sum, sum_v)  # 최대 합 업데이트

print(max_sum)
