#函数的命名方式
a = 10
#开辟了函数空间，不管是否运行了该函数
def fun(a):
    print("abc")#系统自带函数
#此时开始运行定义函数
fun(a)

#内置命名空间 和 全局命名空间
b  = "abc"#全局命名空间，表示在py文件中直接声明出来的变量和函数
print(type(b))#程序中自带的命名空间，如：int str list truple


#局部命名空间
def func(c):
    sum = c#sum就是局部命名
    sum  += c#局部函数只在当前函数中有声明
    return  sum

###作用域：
#        全局作用域：包含全局作用空间和内置作用空间
#          局部作用域： 局部命名空间
###

#globals()函数 locals()函数
print(globals())
print(locals())