N = int(input())
lst = list(map(int, input().split()))

cnt = 0

for num in lst:
    is_prime = True
    if num != 1:
        for i in range(2, num):
            if num % i:
                pass
            else:
                is_prime = False
                break
        if is_prime == True:
            cnt += 1       
print(cnt)