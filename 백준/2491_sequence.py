N = int(input())
seq = list(map(int, input().split()))

cnt1 = 1
cnt2 = 1
max_cnt = 1

for i in range(len(seq)-1):
    if seq[i+1] >= seq[i]:
        cnt1 += 1
    else:
        cnt1 = 1

    if seq[i+1] <= seq[i]:
        cnt2 += 1
    else:
        cnt2 = 1

    max_cnt = max(max_cnt, cnt1, cnt2)
    
print(max_cnt)