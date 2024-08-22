word = input()
cnt = len(word)

for i in range(1, len(word)):
    if word[i] == '=':
        if word[i-1] == 'c':
            cnt -= 1
        elif word[i-1] == 's':
            cnt -= 1
        elif word[i-1] == 'z' and 'dz=' not in word:
            cnt -= 1
    
    if word[i] == 'j':
        if word[i-1] == 'l':
            cnt -= 1
        elif word[i-1] == 'n':
            cnt -= 1

    if word[i] == '-':
        if word[i-1] == 'd':
            cnt -= 1
        elif word[i-1] == 'c':
            cnt -= 1

if 'dz=' in word:
    cnt -= 2

print(cnt)