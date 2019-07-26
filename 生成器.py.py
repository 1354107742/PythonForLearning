#生成器
def fun():
    print("我是周杰伦")
    yield "昆凌"#当函数中有生成器的时候，这就不再是函数了，而是一个生成器函数
g = fun()#通过fun拿到一个生成器
print(g.__next__())#此时完成的功能跟迭代器是一个功能


def func():
    print("我是周杰伦")
    yield "昆凌"
    print("我是王力宏")
    yield "李云迪 "  
    #print("hello")
    #上面的注释代码就不会执行，因为没有yield，所以可以执行但是还是会报错
    #所以一般不会在yield后面书写函数
g1 = func()
print(g1.__next__())
print(g1.__next__())
#所以，yield和return的本质区别在于：
#           yield可以让函数返回结果，分段执行
#           return则是可以返回函数结果