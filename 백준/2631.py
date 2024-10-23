'''
주어진 배열에서 최장 증가 부분 수열(LIS)의 길이를 찾고
이를 통해 필요한 이동 수를 계산하는 방법으로 풀자

-> 원래 배열에서 이미 정렬된 상태에 있는 부분을 찾아 그 길이를 LIS로 사용
-> 총 아이들의 수 - LIS 길이 = 이동해야 할 최소 수
'''

def min_sort(arr, N):
    sorted_arr = sorted(arr)
    lis_length = 0
    dp = [1] * N

    # LIS 길이 계산
    for i in range(N):
        for j in range(i):
            if arr[i] == sorted_arr[j]:  # 정렬된 배열과 일치하면
                dp[i] = max(dp[i], dp[j] + 1)

    lis_length = max(dp)

    return N - lis_length

N = int(input())
arr = list(int(input()) for _ in range(N))
print(min_sort(arr, N))