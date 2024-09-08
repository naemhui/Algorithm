'''
현재 수열 길이 = 이전 수열 길이 + 1
'''

def cnt_seq(idx):
    global cnt
    global max_cnt

    if idx+1 >= A:
        return max_cnt
    
    if sequence[idx+1] < sequence[idx]:
        cnt += 1
        cnt_seq(idx+1)
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
        cnt_seq(idx+1)


A = int(input())
sequence = list(map(int, input().split()))
cnt = 0
max_cnt = 0
print(cnt_seq(0))