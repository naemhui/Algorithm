'''
W를 이루고 있는 g개의 그림문자, 마야 문자열 S
-> W가 S에 들어있을 수 있는 모든 가짓수
즉, S 안에 W의 순열 중 하나가 부분 문자열로 들어있는 경우의 수

g(W의 길이) |S|(S의 길이)
W
S
'''
g, s = map(int, input().split())
W = input().strip()
S = input().strip()

# 알파벳의 개수는 26개 (대소문자 포함시 52개)
# W와 S의 문자 빈도수를 저장
w_count = [0] * 52
s_count = [0] * 52

# 알파벳 인덱스 계산 (대소문자 구분)
def char_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

# W의 문자 빈도수 계산
for c in W:
    w_count[char_index(c)] += 1

# S의 첫 번째 윈도우(길이 g)의 문자 빈도수 계산
for i in range(g):
    s_count[char_index(S[i])] += 1

# 두 배열이 같은지 확인
def is_equal():
    for i in range(52):
        if w_count[i] != s_count[i]:
            return False
    return True

cnt = 0
if is_equal():
    cnt += 1

# 슬라이딩 윈도우 - s 탐색
for i in range(g, s):
    s_count[char_index(S[i])] += 1  # 새로운 문자 추가
    s_count[char_index(S[i - g])] -= 1  # 윈도우에서 벗어난 문자 제거
    
    if is_equal():  # 두 배열이 같으면
        cnt += 1

print(cnt)

