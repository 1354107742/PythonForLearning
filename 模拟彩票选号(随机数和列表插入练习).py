#从37个数字中间选区7个不重复的数字，并加入列表
from random import randint
lis = []
i = 0
while i < 7:
    s = randint(1,37)
    if s not in lis:
        lis.append(s)
        i += 1
print(lis)

