def measure(n):
    lst = []
    for i in range(2, n):
        if n%i == 0:
            lst.append(i)
    if 1 + sum(lst) == n:
        return lst

while True:
    n = int(input())
    if n == -1:
        break
    else:
        if measure(n) == None:
            print(f'{n} is NOT perfect.')
        else:
            print(f'{n} = 1', end='')
            lst = measure(n)
            for m in lst:
                print(f' + {m}', end='')
            print()