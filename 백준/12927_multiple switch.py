light = list(input())
L = len(light)

# if light[0] == 'Y':
#     light[0] = 'N'
#     cnt = 1
# else:
#     cnt = 0

cnt = 0
while 'Y' in light:
    for i in range(L):
        if light[i] == 'Y':
            cnt += 1
            for k in range(i, L, i+1):
                if light[k] == 'Y':
                    light[k] = 'N'
                else:
                    light[k] = 'Y'

print(cnt)