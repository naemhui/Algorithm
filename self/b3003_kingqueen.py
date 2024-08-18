'''
검정 다 있고 흰색 몇 개 사라짐
킹 1 퀸 1 룩 2 비숍 2 나이트 2 폰 8
'''

lst = list(map(int, input().split()))
need = [1, 1, 2, 2, 2, 8]

for n in range(6):
    print(need[n]-lst[n], end=" ")