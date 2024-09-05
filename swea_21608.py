'''
상어 교실 N*N 크기
학생 수 N^2
r행 c열
(1,1) ~ (N,N)
<우선 순위>
1. 좋아하는 학생이 가장 많은 칸으로
2. 인접한 칸 중 비어있는 칸이 많은 칸으로
3. 행 번호가 가장 작은 칸 - 열 번호가 가장 작은 순으로
'''
N = int(input())  # 교실의 크기
arr = [[0]*N for _ in range(N)]  # 교실 배열 (0부터 N-1까지 사용)
dict_like = {}  # 각 학생이 좋아하는 학생 정보를 저장하는 딕셔너리

# 상, 좌, 우, 하 델타 값
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 유효한 좌표인지 확인하는 함수
def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

# 인접한 칸에 좋아하는 학생이 몇 명 있는지 계산하는 함수
def count_likes(student, r, c):
    like_lst = dict_like[student]
    count = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc) and arr[nr][nc] in like_lst:
            count += 1
    return count

# 인접한 빈 칸이 몇 개 있는지 계산하는 함수
def count_empty(r, c):
    count = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc) and arr[nr][nc] == 0:
            count += 1
    return count

# 자리 배정 1단계: 좋아하는 학생이 인접한 칸이 가장 많은 칸 찾기
def seat1(student):
    max_like = -1
    candidates = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:  # 빈 자리일 때
                like_count = count_likes(student, r, c)
                if like_count > max_like:
                    max_like = like_count
                    candidates = [[r, c]]
                elif like_count == max_like:
                    candidates.append([r, c])

    return candidates

# 자리 배정 2단계: 인접한 칸 중 비어있는 칸이 가장 많은 칸 찾기
def seat2(candidates):
    max_empty = -1
    new_candidates = []

    for r, c in candidates:
        empty_count = count_empty(r, c)
        if empty_count > max_empty:
            max_empty = empty_count
            new_candidates = [[r, c]]
        elif empty_count == max_empty:
            new_candidates.append([r, c])

    return new_candidates

# 자리 배정 3단계: 행과 열 번호가 가장 작은 칸 찾기
def seat3(candidates):
    candidates.sort(key=lambda x: (x[0], x[1]))
    return candidates[0]  # 가장 작은 행과 열을 가진 칸 반환

# 학생의 순서에 따라 자리 배정
for _ in range(N * N):
    student, *likes = map(int, input().split())
    dict_like[student] = likes
    candidates = seat1(student)

    if len(candidates) > 1:
        candidates = seat2(candidates)
        if len(candidates) > 1:
            r, c = seat3(candidates)
        else:
            r, c = candidates[0]
    else:
        r, c = candidates[0]

    arr[r][c] = student

# 자리 배정 후 만족도 조사
total_satisfaction = 0
for r in range(N):
    for c in range(N):
        student = arr[r][c]
        satisfaction = count_likes(student, r, c)
        if satisfaction == 1:
            total_satisfaction += 1
        elif satisfaction == 2:
            total_satisfaction += 10
        elif satisfaction == 3:
            total_satisfaction += 100
        elif satisfaction == 4:
            total_satisfaction += 1000

print(total_satisfaction)