from collections import defaultdict
from collections import deque

def set_key():
    return



N = int(input())
options = []
registered_key = set()
word_key = defaultdict(deque)
for i in range(N):
    options.append(input().split())
    
#단축키 사전 : 맵 2개 사용
#단어의 첫번째 글자로 단축키 지정 가능한지 확인
for option in options:
    joined_option = " ".join(option)
    for i, word in enumerate(option):
        low_word = str.lower(word)
        if low_word[0] not in registered_key:
            registered_key.add(low_word[0])
            word_key[joined_option].append((i,0)) #이 옵션의 단축키는 이것입니다.
            break    
# print(word_key)
# print(options)
for option in options:
    joined_option = " ".join(option)
    if joined_option not in word_key.keys():
        for j, word in enumerate(option):
            low_word = str.lower(word)
            flag = False
            for i in range(len(low_word)):
                if low_word[i] not in registered_key:
                    registered_key.add(low_word[i])
                    word_key[joined_option].append((j,i))
                    flag = True
                    break
            if flag:
                break
# print(word_key)
# print(registered_key)

for option in options:
    joined_option = " ".join(option)
    if joined_option not in word_key.keys() or len(word_key[joined_option])==0:
        print(joined_option)
        continue
    word_idx,char_idx = word_key[joined_option].popleft()
    char_list = list(option[word_idx])
    char_list[char_idx] = "["+char_list[char_idx]+"]"
    option[word_idx] = "".join(char_list)
    print(" ".join(option))