def func2(t):
    for i in range(t):
        if 2 ** i > t:
            return i

def func_hemming(a):
    p = [[0] * len(a) for i in range(func2(len(a)))]
    for i in range(len(p)):
        Flag = 1
        for j in range(2 ** i - 1, len(p[i]), 2 ** i):
            for k in range(2 ** i):
                p[i][j + k] = Flag
            Flag ^= 1
    Syn = [0] * func2(len(a))
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == 1:
                Syn[i] ^= a[j]
    for i in range(len(p[0])):
        temp = []
        for j in range(len(p)):
            temp.append(p[j][i])
        if temp == Syn:
            return i + 1
    else:
        return 0

# 88 Вар
# 90 2 44 28 доп. 30
s = [[0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]]
for i in s:
    if func_hemming(i) != 0:
        print('Ошибка в бите ', func_hemming(i))
    else:
        print('Нет ошибок')