'''
문자열이 폭발 문자열을 포함한다면 모든 폭발 문자열 폭발
남은 문자열을 순서대로 이어붙여 새로운 문다열 생성
- 새로 생긴 문자열에 폭발 문자열 포함되어 있을 수도?
- 폭발 문자열이 없어질 때까지 계속
'''
str = input()
explo = input()
stack = []

for s in str:
    stack.append(s)

    # 최근에 추가된 문자들 == 폭발 문자열이면
    if len(stack) >= len(explo) and ''.join(stack[-len(explo):]) == explo:
        stack[-len(explo):] = []  # 폭발 문자열 제거

# 남은 문자열
if stack:
    print(''.join(stack))
else:
    print('FRULA')