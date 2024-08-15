# 원재의 메모리 복구하기

# def modify(memory):
#     if '0' not in memory:
#         return cnt
#     else:
#         for i in range(len(memory)):
#             if i == '1':
#                 memory[i:] = '1'
#                 cnt += 1
def modify(default, memory):
    cnt = 0
    for i in range(len(memory)):
        if memory[i] != default[i]:
            cnt += 1
            if memory[i] == 0:
                default[i:] = [0]*(len(memory)-i)
            else:
                default[i:] = [1]*(len(memory)-i)
            # print(default, memory, cnt)

    return cnt

T = int(input())
for tc in range(1, T+1):
    memory = list(map(int, input()))
    # modify([0]*len(memory), memory)
    result = modify([0]*len(memory) ,memory)
    print(f'#{tc} {result}')