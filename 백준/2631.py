'''
LIS(가장 긴 증가하는 부분수열)을 구하면 해당되는 숫자는 순서에 맞게 자리한 수이기 때문에
이외의 숫자들만 자리에 맞게 옮기면 최소 횟수가 됨
-> LIS 를 구하고, 전체 길이에서 빼주기
'''

N = int(input())

d = [1] * (N+1)  # LIS 저장하는 배열 (d[i] = i번째 수를 끝으로 하는 LIS 길이)
num = [0]  # 수열 저장하는 배열

for i in range(N):
    num.append(int(input()))

# 가장 긴 증가하는 수열 찾기 
# num[j] < num[i]라면, num[i]를 num[j] 뒤에 놓을 수 있으므로
# d[i]는 d[j] + 1과 현재의 d[i] 중 큰 값을 선택
for i in range(1, N+1):
    for j in range(1, i):
        if num[j] < num[i]:
            d[i] = max(d[i], d[j]+1)
# 여기까지 했을 때 d 배열에는 각 인덱스에서 끝나는 최장 증가 부분 수열의 길이가 저장됨

# (최소 이동 횟수 = 전체 수 - 최장 증가 부분수열의 길이)
print(N - max(d))