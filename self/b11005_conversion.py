num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())
answer = ''
while N:
    answer += num[N % B]
    N = N//B

print(answer[::-1])