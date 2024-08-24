N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    check = True
    lst = []

    for w in word:
        if w not in lst:
            lst.append(w)
        if w != lst[-1]:
            check = False
            break

    if check == True:
        cnt += 1

print(cnt)