# lst = []
# for _ in range(9):
#     lst.append(int(input()))
# # print(lst)
# for i in range(9):
#     lst.pop(i)
#     pop1 = lst.pop(i)
#     for j in range(8):
#         lst.pop(j)
#         pop2 = lst.pop(j)
#         lst_sum = sum(lst)

#         if lst_sum == 100:
#             result = sorted(lst)
#             print(''.join(result))
#         else:
#             lst.insert(i, pop1)
#             lst.insert(j+1, pop2)
# IndexError: pop index out of range

#### 위 코드 수정

lst = []
for _ in range(9):
    lst.append(int(input()))

found = False
for i in range(9):
    pop1 = lst.pop(i)
    for j in range(8):
        pop2 = lst.pop(j)
        lst_sum = sum(lst)

        if lst_sum == 100:
            result = sorted(lst)
            for _ in result:
                print(_)
            found = True
            break
        lst.insert(j, pop2)
    lst.insert(i, pop1)
	    
    if found:
        break


#######
# lst = []
# for _ in range(9):
#     lst.append(int(input()))

# for i in range(9):
#     for j in range(i+1, 9):
#         new_lst = []
#         for k in range(9):
#             if k != i and k !=j:
#                 new_lst.append(lst[k])
#                 lst_sum = sum(new_lst)

#                 if lst_sum == 100:
#                     result = sorted(new_lst)
#                     # print(' '.join(map(str, result)))
#                     for _ in result:
#                         print(_)

# lst = []
# for _ in range(9):
#     lst.append(int(input()))

# for i in range(9):
#     for j in range(i+1, 9):
#         new_lst = []
#         for k in range(9):
#             if k != i and k !=j:
#                 new_lst.append(lst[k])
                
#         lst_sum = sum(new_lst)
#         if lst_sum == 100:
#             result = sorted(new_lst)
#             # print(' '.join(map(str, result)))
#             for _ in result:
#                 print(_)


# lst = []
# for _ in range(9):
#     lst.append(int(input()))

# found = False
# for i in range(9):
#     for j in range(i+1, 9):
#         new_lst = []
#         for k in range(9):
#             if k != i and k !=j:
#                 new_lst.append(lst[k])
                
#         lst_sum = sum(new_lst)
#         if lst_sum == 100:
#             result = sorted(new_lst)
#             # print(' '.join(map(str, result)))
#             for _ in result:
#                 print(_)
#             found = True
#             break
#     if found:
#         break