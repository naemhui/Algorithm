def counting(data, temp, k):
    count = [0]*(k+1)

    for num in data:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    for i in range(len(data)-1, -1, -1):
        count[data[i]] -= 1

        temp[count[data[i]]] = data[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    temp = [0]*N
    k = max(data)
    counting(data, temp, k)
    result = ' '.join(map(str, temp))
    
    print(f'#{tc} {result}')