N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
visited = [0] * N

for i in range(N):
    # 확인할 숫자 : target
    target = arr[i]
    left, right = 0, N-1

    while left < right:
        now_sum = arr[left] + arr[right]

        if now_sum == target:
            if left != i and right != i:
                cnt += 1
                break
            else:
                left += 1
                right -= 1

        elif now_sum < target:
            left += 1
        else:
            right -= 1

print(cnt)