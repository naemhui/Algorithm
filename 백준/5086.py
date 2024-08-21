while True:

    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break

    if a == 0 or b == 0:
        print('neither')

    elif a !=0 and b != 0:    
        if b % a == 0:
            print('factor')

        elif a % b == 0:
            print('multiple')
        else:
            print('neither')
