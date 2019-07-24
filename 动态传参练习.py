#接受n 个数字，求这些参数的和
def fun(*el):
    sum =  0
    for i in el:
        sum += i
    return sum
print(fun(6,7))

#写函数，接收两个参数，将极小的数字返回
def min(a,b):
    if a > b:
        return b
    else:
        return a
print(min(1,23))

#接受多个数，返回最大值和最小值  形式要求字典
def func(*args):
    m = args[0] # 假设第0项就是最大值
    mi = args[0]
    for el in args:
        if el > m:
            m = el # 当前这个元素比假设的那个大. 记录当前这个比较大的数
        if el < mi:
            mi = el
    return {"最大值":m, "最小值":mi}
print(func(1,2,3,4,5,6,7,8,9))

#写函数，传入一个参数n，返回n的阶乘
def cal(el):
    cal1 = 1
    i = 1
    if el  == 0:
        return 0
    while i <= el:
        cal1 = cal1 * i
        i += 1
    return cal1
print(cal(5)) 

#输出扑克牌的所有排列
type_of_card = ["红桃","黑桃","方块","草花"]
type_of_num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
def poke(a,b):
    res = []
    for el in a:
        for el1 in b:
            res.append((el,el1))
    return(res)
print(poke(type_of_card,type_of_num))


###输出九九乘法表
i = 1
while i <= 9:
    l = 1
    while i >= l:
        print("%d * %d = %d" %(i,l,i*l), end = "  ")
        l += 1
    print()
    i += 1        