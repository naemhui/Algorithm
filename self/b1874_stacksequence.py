'''
stack 구조: 선입후출
수열 만들기: 스택에 push하는 순서는 오름차순을 지킴
push: +  / pop: -  / 불가능하면 No

8
4
3
6
8
7
5
2
1
'''
8 4 3 6 
stack = []
while True:
    try:
        N = int(input())

        stack.append(N)
        top = stack.pop()
        print(top)

    except EOFError:
        break