'''
P: 계산에서 제외
'''
grades = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
g_sum = 0
c_sum = 0

for _ in range(20):
    S, C, G = map(str, input().split())  # subjects, credits, grades

    if G != 'P':
        g_sum += float(C)*grades[G]
        c_sum += float(C)

print(g_sum/c_sum)