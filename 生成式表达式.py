#可以看出生成了一个生成器
g = (i for i in range(10))
print(g)
#输出一个
print(g.__next__())
print(list(g))
#生成器跟列表推导式不同的地方在于，生成器推导式几乎不占用内存
#生成器推导式仍然是有：惰性机制

#惰性机制演示
def func():
    print(111)
    yield 222
g = func()
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g))
print(list(g1))
print(list(g2))