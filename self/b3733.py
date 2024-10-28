'''
N명의 사람, S개의 주식
'''
while True:
    try:
        N, S = map(int, input().split())
        print(S//(N+1))
    except EOFError:
        break