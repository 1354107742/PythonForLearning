#lambda函数
def func(n):
    return n * n
print(func(3))

a = lambda x:x*x
print(a(3))
#对于简单函数，可以直接用lambda形式直接书写

#sorted函数
lis = [1,2,3,5,7,9,2,4,6,2,7]
lis.sort()
print(lis)
#sorted中的reverse默认是false  改为true变为倒序输出
ll = sorted(lis ,reverse=True)
print(ll)
#sorted中的key 可以自定义排序规则
lis1 = ["啊","哦哦","额呃呃呃"]
def func1 (s):
    return len(s)
ll = sorted(lis1,key = func1)
print(ll)

#filter函数：两个参数  第一个参数是函数 第二个参数是第一个参数的传递
lis2 = ["啊", "哦哦", "额呃呃呃"]
def func2(s):
    return len(s)
ll  = filter(func2,lis2)
#生成一个可迭代器的列表
print(list(ll))

#map函数：对函数进行映射处理
lis3 = [1, 2, 3, 5, 7, 9, 2, 4, 6, 2, 7]
print(list(map(lambda x,y:x+y , lis1,lis2)))
