for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 공통 부분 X
    if x1>p2 or x2>p1 or y1>q2 or y2>q1:
        print('d')
    
    # 점
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1:
            print('c')
            continue

        # 이외 경우는 선
        else:
            print('b')
            continue

    # 점으로 만나는 거 elif 제외 -> 선
    elif q1==y2 or q2==y1:
        print('b')

    else:
        print('a')