def inputPoly():
    a = 1
    x = []
    z = []
    while a != -1:
        y = []
        a = int(input('지수:'))
        b = int(input('계수:'))
        y.append(a)
        y.append(b)
        z.append(a)

        if z.count(a) != 1:
            print('같은 지수가 있습니다')
            z.remove(a)
            y.clear()

        else:
            x.append(y)

        if a == -1:
            x.pop()
            x.sort()
            x.reverse()

            return x


def printPoly(p):
    z = []
    for i in range(len(p)):
        if p[i][1] != 0:
            z.append(p[i])

    k = len(z)
    for i in range(k):
        if i != k - 1:
            if z[i][0] == 1:
                print('%dx' % (z[i][1]), end='')
                print('+', end='')
            else:
                print('%dx^%d' % (z[i][1], z[i][0]), end='')
                print('+', end='')


        else:
            if z[i][0] == 0:
                print('%d' % (z[i][1]))
            elif z[i][0] == 1:
                print('%dx' % (z[i][1]))
            else:
                print('%dx^%d' % (z[i][1], z[i][0]))


def evalPoly(p, x):
    s = 0
    for i in range(len(p)):
        s = s + ((x ** p[i][0]) * p[i][1])

    return s


def addPoly(a, b):
    c = a + b
    c.sort()
    c.reverse()

    k = []

    for i in range(len(c)):
        if c[i][1] != 0:
            k.append(c[i])

    d = []
    n = len(k)
    i = 0

    while i < n - 1:
        if k[i][0] == k[i + 1][0]:
            d.append([k[i][0], k[i][1] + k[i + 1][1]])
            i += 2

        else:
            d.append(k[i])
            i += 1

        if i == n - 1:
            if k[i][0] != k[i - 1][0]:
                d.append(k[i])

    return d


def multiplyPoly(a, b):
    c = a + b
    i = 0
    j = len(a)

    d = []

    while i < len(a):
        j = len(a)
        while j < len(a) + len(b):
            d.append([c[i][0] + c[j][0], c[i][1] * c[j][1]])
            j += 1
        i += 1

    d.sort()
    d.reverse()

    e = []
    n = len(d)
    i = 0

    while i < n - 1:
        if d[i][0] == d[i + 1][0]:
            e.append([d[i][0], d[i][1] + d[i + 1][1]])
            i += 2

        else:
            e.append(d[i])
            i += 1

        if i == n - 1:
            if d[i][0] != d[i - 1][0]:
                e.append(d[i])

    f = []
    n = len(e)
    i = 0

    while i < n - 1:
        if e[i][0] == e[i + 1][0]:
            f.append([e[i][0], e[i][1] + e[i + 1][1]])
            i += 2

        else:
            f.append(e[i])
            i += 1

        if i == n - 1:
            if e[i][0] != e[i - 1][0]:
                f.append(e[i])

    return f


m = 1
P = []
while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    m = int(input('메뉴 선택 (종료시는 9) :'))

    if m == 1:
        print('다항식 입력 선택\n')

        print('다항식 리스트:', inputPoly())


    elif m == 2:
        print('다항식 출력 선택\n')
        P = inputPoly()
        printPoly(P)


    elif m == 3:
        print('다항식 계산 선택\n')
        P = inputPoly()
        print('식:', end='')
        printPoly(P)
        X = int(input('X = '))
        result = evalPoly(P, X)
        print('계산 결과 : ', result)


    elif m == 4:
        print('다항식 덧셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        print('식A:', end='')
        printPoly(A)
        print('식B:', end='')
        printPoly(B)
        C = addPoly(A, B)
        print('덧셈 결과:', end='')
        printPoly(C)


    elif m == 5:
        print('다항식 곱셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        print('식A:', end='')
        printPoly(A)
        print('식B:', end='')
        printPoly(B)
        C = multiplyPoly(A, B)
        print('곱셈 결과:', end='')
        printPoly(C)


    else:
        if m != 9:
            print('메뉴 선택 오류\n')

