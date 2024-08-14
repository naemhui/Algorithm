# def hotel(H, W):
#     result = []
#     for col in range(1, H + 1):
#         for row in range(1, W + 1):
#             number = col * 100 + row
#             result.append(number)
#     return result

T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    # H: 층, W: 가로, N:순서

    floor = N % H
    room = (N // H) + 1
    if floor == 0:
        floor = H
        room -= 1
    print(floor * 100 + room)
