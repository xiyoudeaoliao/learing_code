import random

# 定义空的列表
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = 10
for i in range(10):
    x = random.randint(0, 1)
    if x == 0:
        b -= 1
        if a[b] != 0:
            a[b] = a[b]+1
        else:
            a[b] = 1
    elif x == 1:
        b += 1
        if a[b] != 0:
            a[b] = a[b]+1
        else:
            a[b] = 1
print(a)

