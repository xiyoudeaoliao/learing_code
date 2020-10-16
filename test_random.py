# 写入数据
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
c = [10, 20, 30, 40, 50, 60]


# 定义函数
def a0(j, sita0, sita1, sita2):
    p0 = 0
    p0 = sita1 * a[j] + sita2 * b[j] + sita0
    return p0


def b1(j, sita0, sita1, sita2):
    p0 = 0
    p0 = (sita1 * a[j] + sita2 * b[j] + sita0) * a[j]
    return p0


def c2(j, sita0, sita1, sita2):
    p0 = 0
    p0 = (sita1 * a[j] + sita2 * b[j] + sita0) * b[j]
    return p0


# 随机梯度下降开始计算
def drop():
    buchang = 0.002
    sita_0 = 1
    sita_1 = 1
    sita_2 = 1
    for i in range(1000):
        sita_0 = sita_0 - buchang * a0(1, sita_0, sita_1, sita_2)
        sita_1 = sita_1 - buchang * a0(1, sita_0, sita_1, sita_2)
        sita_2 = sita_2 - buchang * a0(1, sita_0, sita_1, sita_2)
    return sita_0, sita_1, sita_2


x = drop()
print(x)
