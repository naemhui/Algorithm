# def selection_sort(arr, N):
#     for i in range(N-2):
#         min_idx = i
#         for j in 

def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0][0]
    low = []
    high = []
    for i in range(1, len(arr)):
        value = arr[i][0]
        if value < pivot:
            low.append(arr[i])
        else:
            high.append(arr[i])

    return qsort(low) + [arr[0]] + qsort(high)


N = int(input())
arr = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    arr.append([age, name])

arr = qsort(arr)
for member in arr:
    print(*member)