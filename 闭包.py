name1 = "inpex"#接下来，会解释为什么全局变量是不安全的  
def func():
    name = "alex"#常驻内存
    def inner():
        print(name)#内层函数调用外部函数变量，叫做闭包
    return inner


ret = func()
ret()#执行的inner()
#闭包的用处：就是让函数的部分变量常驻内存


#虽然全局函数也可以做到同样的效果，但是！
#闭包的第二个用处：保证数据安全性
#                   如果要修改闭包内的常驻内存，那么
#                   只有在同一函数中进行修改
#                   所以数据更加安全
def abc():
    global name1
    name1  = "呵呵"
    print(name1)
abc()


