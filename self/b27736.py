N = int(input())

lst = list(map(int, input().split()))

if lst.count(1) > lst.count(-1):
    print('APPROVED')

elif lst.count(0) >= N//2:
    print('INVALID')

else:
    print('REJECTED')