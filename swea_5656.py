'''
구슬 dfs
중력

'''

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    if 0<=r<H and 0<=c<W:
        return True
    return False

def breaking(array)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())  # W열*H행 배열
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    print(f'#{tc} {ans}')