'''
별똥별 수 최소화
트램펄린 L*L
'''
n, m, l, k = map(int, input().split())

stars = []
for _ in range(k):
    x, y = map(int, input().split())
    stars.append((x, y))

bounce = 0  # 튕겨낸 별똥별 최대 수

# 각 별똥별을 기준으로 트램펄린을 배치할 수 있는 모든 가능한 좌표를 확인
for starA in stars:  # 트램펄린의 가로 위치 결졍 (별똥별 A 기준)
    for starB in stars:  # 트램펄린의 세로 위치 결정 (별똥별 B 기준)
        cnt = 0
        # 트램펄린의 왼쪽 아래 모서리 좌표가 (starA[0], starB[1])인 경우
        x1, y1 = starA[0], starB[1]

        # 트램펄린 범위 안에 들어오는 별똥별을 세기
        for starC in stars:
            if x1 <= starC[0] <= x1 + l and y1 <= starC[1] <= y1 + l:
                cnt += 1

        # 최대로 튕겨낸 별똥별 수 갱신
        bounce = max(bounce, cnt)

# 튕겨내지 못한 별똥별의 수 출력
print(k - bounce)