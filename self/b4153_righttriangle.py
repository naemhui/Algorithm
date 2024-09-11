while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break  # 세 수가 0이면 break

    nums = sorted(nums)

    if nums[0]*nums[0] + nums[1]*nums[1] == nums[2]*nums[2]:
        print('right')

    else:
        print('wrong')