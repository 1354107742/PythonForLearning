def func():
    print("大碴粥")
    a = yield "great"
    print("麻花")
    b = yield "good"


g = func ()
#.send()功能和.__next__()功能大致相同
#但是最大的区别在于，send.()会给与你的上一个yield传值
print(g.__next__())
#同样，因为send()因为只能给上一个传值，所以！！！！
#第一个绝对不能用yield 最后一个也不可以用yield
print(g.send( 1 ))

#将生成器转换为列表
def fun2():
    yield 11
    yield 22
    yield 33
    yield 44
g = fun2
lst = list(g) #这样可以转化
print(lst)