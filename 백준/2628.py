W, L = map(int, input().split())
N = int(input())
width = [0, L]
length = [0, W]

for i in range(N):
    ex, num = map(int, input().split()) 
    if ex==0:
        width.append(num)
    elif ex==1:
        length.append(num)

width.sort()
length.sort()

max_v = 0

for w in range(len(width)-1):
    for l in range(len(length)-1):
        area = (width[w+1]-width[w])*(length[l+1]-length[l])
        if  area> max_v:
            max_v = area

print(max_v)
