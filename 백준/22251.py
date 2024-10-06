'''
1~N층
K자리 수(칸)
최소 1 ~ 최대 P개 반전
현재 x층
'''
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
numbers = []
arr = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011', '1011111', '1110000', '1111111', '1111011']
for i in range(10):
    numbers.append(list(arr[i]))

N, K, P, X = map(int, input().split())

X = str(X)
leds = []  # 현재 전광판 led
for i in range(len(X)):
    idx = int(X[i])
    leds.append(numbers[idx])

result = 0  # 경우의 수
# num: 현재 숫자
def switch(num):
    # candidate = []
    for digits in range(K-1, -1, -1):
        cnt = 0  # 경우의 수 (P 초과 시 )
        # 현재 숫자 = numbers[num] ex. ['0', '1', '1', '0', '0', '0', '0']
        # can : 후보자
        for can in numbers:
            for i in range(7):
                if numbers[num][i] != can[i]:
                    cnt += 1
            if cnt <= P and can != numbers[num]:
                
            # N보다 작은지 어떻게 확인하지 그냥 마지막에 확인할까