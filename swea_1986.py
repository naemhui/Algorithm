t = int(input())

for i in range(1, t+1):

    n = int(input())
    lst = []

    for j in range(1, n+1):
        
        if j % 2 == 0:
            lst.append((-1)*j)
        else:
            lst.append(j)

    print(f'#{i} {sum(lst)}')