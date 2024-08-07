T = int(input())
# arr = [[0]*(1000) for _ in range(1000)]
data = [list(map(int, input().split())) for _ in range(T)]
# for t in range(T):
#     x, y, w, h = map(int, input().split())
# area += w*h
lst = []
result = []
for i in range(T):
    for x in range(data[i][0], data[i][0] + data[i][2]):
        for y in range(data[i][1], data[i][1] + data[i][3]):
            lst.append([x, y])
    result.append(lst)

# print(lst)  # lst에 해당 위치 모두 들어감

# i = T-1
# while i < T:
for i in range(T-1, -1, -1):  # T = 3이면 2 1 0
    print('직사각형 번호:', i+1, len(result[i]))

    # i가 1이면 result[1]에 result[2] 들어있는 거 다 빼고 len(result[1])출력
    for n in range(len())
