B_num = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
B_alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

N, B = input().split()
b = int(B)
result = 0

for i in range(len(N)):
    # 1. 숫자인 경우
    if N[i].isdigit(): 
        num = int(N[i])
    # 2. 알파벳인 경우
    else:
        num = B_num[B_alp.index(N[i])]
    result += num * b**(len(N)-1-i)

print(result)