N = int(input())
lst = list(map(int, input().split()))
order = [str(i) for i in range(1, N + 1)]

for i in range(len(lst)):
    num = order.pop(i)
    order.insert(i-lst[i], num)

for _ in order:
    print(_, end=' ')