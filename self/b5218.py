alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

for _ in range(int(input())):
    word1, word2 = input().split()
    ans = [0]*len(word1)
    
    for i in range(len(word1)):
        if alpha[word1[i]] > alpha[word2[i]]:
            ans[i] = alpha[word2[i]] - alpha[word1[i]] + 26
            
        else:
            ans[i] = alpha[word2[i]] - alpha[word1[i]]

    # print('Distances:', f'{ans[0]} {ans[1]} {ans[2]} {ans[3]}')
    print('Distances:', *ans)