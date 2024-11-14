num = int(input())
number = str(num)

if '7' not in number:
    if num % 7 == 0:
        print(1)
    else:
        print(0)

else:
    if num % 7 == 0:
        print(3)
    else:
        print(2)