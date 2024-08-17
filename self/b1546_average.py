N = int(input())
score = list(map(int, input().split()))

max_v = max(score)
avg = (sum(score)/max_v*100)/N
print(avg)