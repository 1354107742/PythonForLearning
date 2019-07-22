#利用函数将列表中的奇位数放到新的列表中输出
list = [1,2,3,4,5,6,7,8,9]
lis2 = []
def fun(lis):
    for i in range(len(lis)):
        if i % 2 == 0:
             lis2.append(lis[i])
fun(list)
print(lis2)


#判断用户输入对象是否大于5
n = input("请输入你想要输入的内容:")

def func( n1 ):
    if len( n1) > 5:
        return True
    else:
        return False
func(n)


