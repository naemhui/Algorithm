N = int(input())
arr = list(map(int,input().split()))
t = arr.count(1)
f = arr.count(-1)
m = arr.count(0)
if m * 2 >= N:
    print("INVALID")
elif t > f:
    print("APPROVED")
else:
    print("REJECTED")