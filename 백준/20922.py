'''
같은 원소가 K개 이하로 들어있는 최장 연속 부분수열의 길이
'''
N, K = map(int, input().split())
seq = list(map(int, input().split()))
result = 0
# cnts = [0] * 200001
cnts = [0] * (max(seq)+1)
start, end = 0, 0

while end < N:
    # 겹치는 거 싫어!
    if cnts[seq[end]] < K:
        cnts[seq[end]] += 1
        end += 1

    # 겹쳐버렸다면 시작 포인터 이동
    else:
        cnts[seq[start]] -= 1
        start += 1

    result = max(end-start, result)

print(result)