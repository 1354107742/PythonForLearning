#列表推导式
#语法 [最终结果{变量}for 变量 in 可迭代对象]
lis = ['python%s' %i for i in range (1,15)]
print(lis)


#获取100以内能被3整除的数
lis = ["%d" %i for i in range (1,100) if i % 3 == 0 ]
print(lis)

#获取名字中有两个e的名字
name = ["tom","joee","honey","steven"]
list1 = [first for first in name if first.count("e") == 2]
print(list1)
