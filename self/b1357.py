X, Y = map(str, input().split())

X = X[::-1]
Y = Y[::-1]
# print(X, Y)
# print(int(Y))
NEW = str(int(X) + int(Y))
print(int(NEW[::-1]))