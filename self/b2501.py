N, K = map(int, input().split())
lst = []
for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)
try:
    if lst[K]:
        print(lst[K-1])
except:
    print(0)