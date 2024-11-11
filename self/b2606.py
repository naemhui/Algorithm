N = int(input())  # 컴퓨터 수
C = int(input())  # 컴퓨터 쌍의 수

visited = [0] * (N+1)
for _ in range(C):
    