import numpy as np

# 写入数据
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 4, 3, 5, 6, 7, 9, 8]
c = [12, 24, 45, 67, 89, 90, 89, 98]

m = len(a)


# 定义函数 来更新当前所计算系数下的和的偏导值
def a0(n, sita_1, sita_2, sita_0):
    p0 = 0
    for i in range(n):
        p0 = a[i] * sita_1 + b[i] * sita_2 + sita_0 - c[i]
    return p0


def b1(n, sita_1, sita_2, sita_0):
    p0 = 0
    for i in range(n):
        p0 = (a[i] * sita_1 + b[i] * sita_2 + sita_0 - c[i]) * a[i]
    return p0


def c2(n, sita_1, sita_2, sita_0):
    p0 = 0
    for i in range(n):
        p0 = (a[i] * sita_1 + b[i] * sita_2 + sita_0 - c[i]) * b[i]
    return p0


def line():
    buchang = 0.001
    sita_0 = 1
    sita_1 = 1
    sita_2 = 1
    for i in range(5000):
        sita_0 = sita_0 - (1 / m) * buchang * a0(m, sita_0, sita_1, sita_2)
        sita_1 = sita_1 - (1 / m) * buchang * b1(m, sita_0, sita_1, sita_2)
        sita_2 = sita_0 - (1 / m) * buchang * c2(m, sita_0, sita_1, sita_2)

    return sita_0, sita_1, sita_2


def price(sita_0, sita_1, sita_2, x1, x2):
    y = sita_0 + sita_1 * x1 + sita_2 * x2
    print(y)


n = line()
print(n)
price(n[0], n[1], n[2], 10, 20)

