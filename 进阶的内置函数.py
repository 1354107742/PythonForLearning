#callable()#判断是否能调用
a = 10
def func():
    print(b)
print(callable(a))
print(callable(func))

#eval（）动态执行字符串类型的代码
s =  input("计算加法：")
s1 = input("计算乘法：")
print(eval(s))
print(eval(s1))
##主要可以返回一个计算后的数

#exec() 也是动态执行
#与eval()相比，他可以执行代码和更加复杂的运算
s = "for i in range(10):print(i)"
print(exec(s))