n = int(input())
lst = ['3', '6', '9']

for i in range(1, n+1):
    count = 0
    
    for j in str(i):
        if j in lst:
            count += 1

    if count > 0:
        i = '-' * count

    print(i, end=' ')

# for i in range(1, 30):
#     lst = []
#     int(num = )str(i)
#     if len(int(num) =)= 1:
#         if int(num ==) '3' or int(num ==)'6' or int(num ==)'9':
#             # lst.appned('-')
#             print('-')
#         else:
#             print(int(num)
#)     else:
#         for j in range(len(int(num)):)
#             if int(num[j]) == '3' or int(num ==)'6' or int(num ==)'9':
#                 lst.append('-')
#             else:
#                 print(int(num[j]))
    # print(lst)

#####################

# for i in range(1, n+1):
    # num = str(i)
    # # 1자리수
    # if len(num)== 1:
    #     if num == '3' or num =='6' or num =='9':
    #         print('-')
    #     else:
    #         print(i)
    # elif num[1] == 0 or num[2] ==0:
    #     print(i)
    # else:
    #     # 2자리수
    #     if len(num) == 2:
    #         if int(num[0]) % 3==0:
    #             if int(num[1]) % 3 == 0:
    #                 print('--')
    #             else:
    #                 print('-')
    #         elif int(num[1]) % 3 == 0:
    #                 print('-')
    #         else:
    #             print(i)

    #     # 3자리수
    #     if len(num) == 3:
    #         if int(num[0]) % 3 == 0:
    #             if int(num[1]) % 3 == 0 and int(num[2]) % 3 == 0:
    #                 print('---')
    #             elif int(num[1]) % 3 == 0 or int(num[2]) % 3 == 0:
    #                 print('--')
    #             else:
    #                 print('-')
    #         elif int(num[1]) % 3 == 0:
    #             if int(num[2]) % 3 == 0:
    #                 print('--')
    #             else:
    #                 print('-')
    #         elif int(num[2]) % 3 == 0:
    #             print('-')
    #         else:
    #             print(i)
            

##############33
# n = int(input())

# for i in range(1, n+1):
#     num = str(i)
#     # 1자리수
#     if len(num)== 1:
#         if num == '3' or num =='6' or num =='9':
#             print('-')
#         else:
#             print(num)
  
#     # 2자리수
#     if len(num) == 2:
#         if num[1] == 0:
#             if int(num[0]) % 3 == 0:
#                 print('-')
#             else:
#                 print(i)
#         elif int(num[0]) % 3==0:
#             if int(num[1]) % 3 == 0:
#                 print('--')
#             else:
#                 print('-')
#         elif int(num[1]) % 3 == 0:
#                 print('-')
#         else:
#             print(num)

#     # 3자리수
#     if len(num) == 3:
#         if num[1] == 0:
#             if i % 3 == 0:
#                 print()
            
            
#             num[2] == 0:
#             print(i)





#         else:
#             if int(num[0]) % 3 == 0:
#                 if int(num[1]) % 3 == 0 and int(num[2]) % 3 == 0:
#                     print('---')
#                 elif int(num[1]) % 3 == 0 or int(num[2]) % 3 == 0:
#                     print('--')
#                 else:
#                     print('-')
#             elif int(num[1]) % 3 == 0:
#                 if int(num[2]) % 3 == 0:
#                     print('--')
#                 else:
#                     print('-')
#             elif int(num[2]) % 3 == 0:
#                 print('-')
#             else:
#                 print(num)



# ##############
# n = int(input())

# for i in range(1, n+1):
#     count = 0

#     if len(str(i)) == 1:
#         if i % 3 == 0:
#             print('-')
#         else:
#             print(i)

#     elif (i//10) % 3 == 0:
#         if (i - i//10)


