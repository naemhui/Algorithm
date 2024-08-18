word = input()
N = len(word)
ans = 1
for i in range(N//2):
    if word[i] != word[(-1)*i-1]:
        ans = 0

print(ans)