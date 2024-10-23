'''
두 포인터 : left, right
left : 가장 작은 원소 -> 큰 원소
right : 가장 큰 원소 -> 작은 원소

왜?
-> 두 수의 합이 target보다 작으면 left를 증가,
-> target보다 크면 더 작은 수를 사용하기 위해 right를 감소
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for i in range(N):
    # 확인할 숫자 : target
    target = arr[i]
    left, right = 0, N-1

    while left < right:
        now_sum = arr[left] + arr[right]

        if now_sum == target:
            # 자기 자신(target) 제외한 두 수인지
            if left != i and right != i:
                cnt += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1
            # # target이 left 또는 right와 같으면
            # else:
            #     left += 1
            #     right -= 1

        elif now_sum < target:
            left += 1
        else:
            right -= 1

print(cnt)