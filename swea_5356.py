def is_valid(i, j, N, M):
    return 0<=i<N  and 0<=j<M

T = int(input())

for tc in range(1, T+1):
    board = [list(input()) for _ in range(5)]
    arr = [[0]*15 for _ in range(15)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            arr[i][j] = board[i][j]
    # print(arr)
    
    word = ''
    for c in range(15):
        for r in range(15):
            if arr[r][c] != 0:
                word += arr[r][c]
            # print(arr[r][c], end="")
    print(f'#{tc} {word}')

'''
#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''
            # print(board[i][j], end="")

                # print(k[i], end=" ")

    # for k in board:
    #     for j in range(len(k)):
    #         for i in range(5):
    #             if is_valid(i,j,5,len(k)):    
    #                 arr[i][j] = board[i][j]
    # print(arr)

    # print(f'#{tc} {result}')