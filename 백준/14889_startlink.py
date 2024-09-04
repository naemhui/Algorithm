'''
N명 -> N/2
'''

N = int(input())
arr = [list(map(int, input().split()) for _ in range(N))]
# lst = []
n = 2  # 원소 2개인 조합

lst2 = []
def ability_differ(lst1):
    for i in range(N):
        if i not in lst1:
            lst2.append(i)

    # print(lst1)
    start_ability = arr[lst1[0]][lst1[1]] + arr[lst1[1]][lst1[0]]
    link_ability = arr[lst2[0]][lst2[1]] + arr[lst2[1]][lst2[0]]

    return abs(start_ability-link_ability)


differ_lst = []

def run(lev, start, lst):
    if lev == n:
        lst = list(lst)
        differ = ability_differ(lst)
        differ_lst.append(differ)
        return

    for i in range(start, N):
        lst.append(arr[i])
        run(lev + 1, i + 1, lst)
        lst.pop()

run(0, 0, [])
print(differ_lst)