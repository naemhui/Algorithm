A, B = input().split()

AS = int(A[::-1])
BS = int(B[::-1])

print(max(AS, BS))