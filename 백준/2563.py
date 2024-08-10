N = int(input())
arr = list([0]*101 for _ in range(101))

for _ in range(N):
    r, c = map(int, input().split())
    
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1

result = 0
for _ in range(101):
    result += arr[_].count(1)
print(result)