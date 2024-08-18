N = 4
bucket = list(i for i in range(1, N+1))
print(bucket)
print(bucket[3:1:-1])
bucket[1:3] = bucket[2:0:-1]
print(bucket)