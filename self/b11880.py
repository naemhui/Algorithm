from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    sides = list(map(int, stdin.readline().split()))
    max_side = max(sides)
    total = (sum(sides)-max_side)**2 + max_side**2
    print(total)