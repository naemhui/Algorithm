N = int(input())

for i in range(1, N+1):
    num = sum((map(int, str(i))))
    num_sum = i + num  # 분해합

    if num_sum == N:
        print(i)
        break
    if i == N:  # 생성자 없음
        print(0)