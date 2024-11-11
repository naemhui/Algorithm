N = int(input())
size_lst = list(map(int, input().split()))
T, P = map(int, input().split())

shirt = 0
pen1 = 0
pen2 = 0

for size in size_lst:
    if size % T >0:
        shirt += size // T + 1
    else:
        shirt += size // T
    
pen1 = N // P
pen2 = N % P

print(shirt)
print(pen1, pen2)