import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

# LIS를 저장할 리스트
lis = []

for x in num:
    pos = bisect_left(lis, x)  # x가 들어갈 위치를 찾음
    if pos == len(lis):
        lis.append(x)  # 새로운 요소 추가
    else:
        lis[pos] = x  # 기존 요소 대체

print(len(lis))  # 최장 증가 부분 수열의 길이 출력