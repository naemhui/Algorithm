'''
2018로만 이루어짐 - 관련있는 
2 0 1 8 모두 포함 - 밀접
각 개수 같음 - 묶여있는
else: 관련 없는 0
'''

number = input()

is_related = True
for n in number:
    if n not in '2018':
        is_related = False

is_closely = True
if is_related:
    for i in '2018':
        if i not in number:
            is_closely = False

is_tied = False
if number.count('2') == number.count('0') == number.count('1') == number.count('8'):
    is_tied = True

if is_related:
    if is_closely:
        if is_tied:
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)