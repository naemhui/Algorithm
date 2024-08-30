def is_primenumber(number):
    if number == 1:
        return False
    else:
        for i in range(2, number):
            if number%i == 0:
                return False
        return True

# print(is_primenumber(6))
M = int(input())
N = int(input())
prime_lst = []

for i in range(M, N+1):
        
    if is_primenumber(i) == True:
        prime_lst.append(i)

# print(prime_lst)
if prime_lst:
    print(sum(prime_lst))
    print(min(prime_lst))
else:
    print(-1)