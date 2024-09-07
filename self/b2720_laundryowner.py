'''
거스름돈의 액수 -> 0.25 / 0.1 / 0.05 / 0.01의 개수를 구하기
거스름돈 <= 0.05
'''
coin = [25, 10, 5, 1]
change = []

T = int(input())
for tc in range(T):
    C = int(input())

    for c in coin:
        if c:
            change.append(C//c)
            C = C%c
        else:
            break
    print(*change)
    change = []