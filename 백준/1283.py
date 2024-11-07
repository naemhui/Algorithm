'''
첫 글자가 리스트 안에 있는지 확인
없으면 리스트에 추가, 있으면 

단축키 저장
'''
short = []

N = int(input())
for _ in range(N):
    words = list(input().split())
    is_end = False
    
    for i in range(len(words)):
        if words[i][0].upper() not in short:
            short.append(words[i][0].upper())
            is_end = True
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            # print(' '.join(words)) 
            break


    # 여기까지 왔따는 건 모든 단어의 첫글자 등록 실패
    if not is_end:
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if words[i][j].upper() not in short:
                    short.append(words[i][j].upper())
                    is_end = True
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]
                    break
            if is_end:
                break

    print(' '.join(words))
