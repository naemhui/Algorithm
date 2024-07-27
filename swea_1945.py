# 최종 제출 코드
t = int(input())

def factor(n, i):
    count_2 = 0
    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0
    
    while n % 2 == 0:
        n //= 2
        count_2 += 1

    while n % 3 == 0:
        n //= 3
        count_3 += 1

    while n % 5 == 0:
        n //= 5
        count_5 += 1

    while n % 7 == 0:
        n //= 7
        count_7 += 1

    # count_11 = 0
    while n % 11 == 0:
        n //= 11
        count_11 += 1

    print(f'#{i} {count_2} {count_3} {count_5} {count_7} {count_11}')

for i in range(1, t+1):
    n = int(input())
    result = factor(n, i)

##################
# 2. 첫 번째 pass 코드
# def factor(n):
#     count_2 = 0
#     count_3 = 0
#     count_5 = 0
#     count_7 = 0
#     count_11 = 0
    
#     while n % 2 == 0:
#         n //= 2
#         count_2 += 1
#     n_2 = n
#     # return count_2

#     # count_3 = 0
#     while n_2 % 3 == 0:
#         n_2 //= 3
#         count_3 += 1
#     n_3 = n_2

#     # count_5 = 0
#     while n_3 % 5 == 0:
#         n_3 //= 5
#         count_5 += 1
#     n_5 = n_3

#     # count_7 = 0
#     while n_5 % 7 == 0:
#         n_5 //= 7
#         count_7 += 1
#     n_7 = n_5

#     # count_11 = 0
#     while n_7 % 11 == 0:
#         n_7 //= 11
#         count_11 += 1

#     print(f'{count_2} {count_3} {count_5} {count_7} {count_11}')
#     # return count_2, count_3, count_5, count_7, count_11

# n = 6791400
# result = factor(n)


##############
# 3. 내 최종 코드를 봤을 때 똑같은 코드가 너무 반복되는 것 같아서 GPT한테 줄여달라고 했다
# t = int(input())

# def factor(n, i):
#     factors = [2, 3, 5, 7, 11]
#     counts = []

#     for factor in factors:
#         count = 0
#         while n % factor == 0:
#             n //= factor
#             count += 1
#         counts.append(count)
    
#     print(f'#{i} {" ".join(map(str, counts))}')

# for i in range(1, t+1):
#     n = int(input())
#     factor(n, i)



#########################
# 4. 함수 내, print -> return
# 함수 안에서 return 대신 print를 쓴 게 마음에 걸렸다 ..
# t = int(input())

# def factor(n, i):
#     factors = [2, 3, 5, 7, 11]
#     counts = []

#     for factor in factors:
#         count = 0
#         while n % factor == 0:
#             n //= factor
#             count += 1
#         counts.append(count)
    
#     print(f'#{i} {" ".join(map(str, counts))}')

# for i in range(1, t+1):
#     n = int(input())
#     factor(n, i)




#########################
# 시도 코드
# t =  int(input())

# for i in range(t):

## count 
# 1525
# n = 540
# count2 = 0
# while n // 2:
#     count2 += 1

# lst = []
# if n % 2 != 0:
#     count2 += 1
#     lst.append()

# while n // 2 != None:
# if n // 2:
    # print(n/2)