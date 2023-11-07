import sys
sys.setrecursionlimit(10000)
def func(C):
    s = [0] * fib1(C, 1, 2, 1)
    s[-1] = 1
    C -= fib2(C, 1, 2)
    while C > 0:
        s[fib1(C, 1, 2, 0)] = 1
        C -= fib2(C, 1, 2)
    return s

def fib1(C, f1, f2, cnt):
    if C >= f2:
        return fib1(C, f2, f1 + f2, cnt + 1)
    else:
        return cnt
def fib2(C, f1, f2):
    if C >= f2:
        return fib2(C, f2, f1 + f2)
    else:
        return f1
def dop(C):
    temp = 0
    p = str(C)[::-1]
    for i in range(len(p)):
        if p[i] == '1':
            temp += fib3(i, 1, 2, 0)
    return temp
def fib3(k, f1, f2, cnt):
    if k != cnt:
        return fib3(k, f2, f1 + f2, cnt + 1)
    else:
        return f1
print(dop(int(input())))
