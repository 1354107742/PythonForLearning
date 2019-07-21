#函数包括函数名，函数体，参数，和返回值


#现在举例一个函数体
def yue(way,age):#way就是参数，因为这个赋值本身没有任何意义，所以这个是个形参
    print("打开方式%s" %way)
    print("大妈%s"%age)
    print("萝莉")
    print("大叔")
    print("女装大佬")


def buyue(way, age = "36"):  # way就是参数，因为这个赋值本身没有任何意义，所以这个是个形参
    print("打开方式%s" % way)
    print("大妈%s" % age)
    print("萝莉")
    print("大叔")
    print("女装大佬")

#参数分为实参和形参
yue("探探",36)#程序内就是参数，但是这个是实参，因为有具体的意义
yue("默默",40)#同样也参数

#参数可以有默认参数
buyue("默默")
buyue("默默","33")
