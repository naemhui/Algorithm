while True:
    num = input()
    if num == '0':
        break

    else:
        is_palin = True
        for i in range(len(num)//2):
            if num[i] != num[len(num)-i-1]:
                is_palin = False
                print('no')
                break
        if is_palin == True:
            print('yes')