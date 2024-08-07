def graph(data, T):
    arr = [[0]*1001 for _ in range(1001)]
    for i in range(T):
        for x in range(data[i][0], data[i][0] + data[i][2]):
            for y in range(data[i][1], data[i][1] + data[i][3]):
                arr[x][y] = i+1

    return arr

def area(arr):
    count = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == _+1:
                count += 1
    # return count
    print(count)

T = int(input())
data = [list(map(int, input().split())) for _ in range(T)]
arr = graph(data, T)
count = 0

for _ in range(T):
    count = 0
    area(arr)
    # result = area(arr)
# print(result)