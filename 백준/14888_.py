'''
수열 N개, 연산자 N-1개
연산자 우선순위 무시, 나눗셈은 몫만 취함
'''
N = int(input())
num_lst = list(input().split())
oper_lst = list(map(int, input().split()))  # + - * //
# O = ['+', '-', '*', '//']
# operator = []

max_v, min_v = -1e9, 1e9

def dfs(idx, total, plus, minus, multi, divide):
    global max_v, min_v

    if idx == num_lst:
        max_v, min_v = max(total, max_v), min(total, min_v)
        return
    
    # 연산 하나씩 하기
    if plus:
        dfs(idx+1, total+num_lst[idx], plus-1, minus, multi, divide)

    if minus:
        dfs(idx+1, total-num_lst[idx], plus, minus-1, multi, divide)

    if multi:
        dfs(idx+1, total*num_lst[idx], plus, minus, multi-1, divide)

    if divide:
        dfs(idx+1, int(total/num_lst[idx]), plus, minus, multi, divide-1)

dfs(1, num_lst[0], oper_lst[0], oper_lst[1], oper_lst[2], oper_lst[3])
print(max_v)
print(min_v)