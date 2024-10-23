'''
선택 정렬 문제인가 이거
'''

def selection_sort(arr, N):
    cnt = 0

    for i in range(N-2):
        # min_idx = arr[min(arr)]
        min_idx = i  # 최솟값 위치를 기준위치로
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # 구간의 최솟값을 기준위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        cnt += 1

        if arr == sorted(arr):
            return cnt

N = int(input())
arr = list(int(input()) for _ in range(N))
print(selection_sort(arr, N))