N, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
# distance[i] == i 위치까지 운전한 최솟값
distance = [i for i in range(D+1)]

# i번째 위치에 도달하는 최솟값 구하기
for i in range(D+1):
    # 최단거리 갱신: i번째 위치에 도달하는 최솟값 구하기
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)

    # 지름길 고려: end가 고속도로 범위 내이고&최솟값이 end에 저장된 값보다 작다면 갱신
    for start, end, short in lst:
        if i == start and end <= D and distance[i]+short < distance[end]:
            distance[end] = distance[i]+short

print(distance[D])