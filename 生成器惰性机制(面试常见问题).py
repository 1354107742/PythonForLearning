def add(a, b):
    return a + b


def test():
    for r_i in range(4):
        yield r_i


g = test()

for n in [2, 10]:
    g = (add(n, i) for i in g)#问题所在
    #作为一个生成器，只有到最后的 时候才会取值、
    #n  = 2
    #第一步：g = (add(n, i) for i in test())
    #n = 10
    #第二步：g = (add(n, i) for i in (add(n, i) for i in test()))
    #g = (add(10, i) for i in (add(10, i) for i in [0,1,2,3]))

print(list(g))
