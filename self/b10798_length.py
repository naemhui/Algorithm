<<<<<<< HEAD
board = [list(input()) for _ in range(5)]
arr = [[0]*15 for _ in range(15)]

for i in range(len(board)):
    for j in range(len(board[i])):
        arr[i][j] = board[i][j]
    
word = ''
for c in range(15):
    for r in range(15):
        if arr[r][c] != 0:
            word += arr[r][c]
=======
board = [list(input()) for _ in range(5)]
arr = [[0]*15 for _ in range(15)]

for i in range(len(board)):
    for j in range(len(board[i])):
        arr[i][j] = board[i][j]
    
word = ''
for c in range(15):
    for r in range(15):
        if arr[r][c] != 0:
            word += arr[r][c]
>>>>>>> 6359f9d65740511ff3257821461c2814158000e1
print(word)