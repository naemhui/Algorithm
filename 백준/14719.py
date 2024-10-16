H, W = map(int,input().split())
lst = list(map(int,input().split()))
result = 0

for i in range(H):
    cnt = 0  # 빈칸 세기
    x = False  # 빗물이 고일 수 있는지

    for j in range(len(li)):
        if lst[j] != 0:
            x = True
            lst[j] -= 1  # 블록 높이 -1
            result += cnt
            cnt = 0  # 빗물 고임
        elif x == True:
            cnt += 1

print(result)