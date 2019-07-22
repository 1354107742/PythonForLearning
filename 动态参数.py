####这种情况下必须要传输两个参数####
def breakfast(good,bad):
    print("我要吃",good,bad)
breakfast("炸鸡","啤酒")

###动态参数可以活性的赋予参数值
###位置参数 > 动态参数
###如果同时有两种参数，要先写位置参数
###如果有默认参数,必须放在最后面才能生效，并且必须指定id才能修改
def lunch(*food):
    print("我要吃", food)
lunch("炸鸡", "啤酒")

###编写一个函数，传输任意一个整数，返回这些整数的和
def s_um(*value):
    sum = 0
    for i in value:
        sum += i
    return sum
print(s_um(1,2,3,4,5))


###动态接受关键字参数
###   *位置参数
###   **动态参数
###动态参数传入的参数格式是字典形式
def afterice(**food):
    print(food)
afterice(goodfood = "盖浇饭",badfood = "冰淇凌")



