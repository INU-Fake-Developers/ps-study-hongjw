def summatrix(a):             #정방 행렬에서 상위 삼각행렬 더하는 코드!
    i = 0
    j = 0
    n = len(a)
    s = 0

    while i < n:
        j = 0
        while j < n:
            if i < j:
                s += a[i][j]
            j += 1
        i += 1

    return s


import random

m = int(input('정방 행렬의 크기:'))
x = []
for j in range(m):
    y = []
    for i in range(m):
        y.append(random.randint(0, 3))
    x.append(y)

for i in range(m):
    x[i][i] = 0

for i in range(m):
    for j in range(m):
        print(x[i][j], end=' ')
    print()

print(summatrix(x))