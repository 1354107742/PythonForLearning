lis1 = ["金毛狮王","白眉鹰王","紫衫龙王","青衣福王"]

#引入赋值
lis2 = lis1#列表
lis2.append("杨左使")
#增加了新的变量
print(lis2)
#也增加了这个新变量
print(lis1)
#实际是指向了一个同一个地址，内存中只有一个变量列表，两个变量指向同一个变量
#所以对其中一个变量进行操作，其中也会操作
#验证方法
print(id(lis1))
print(id(lis2))
#地址是相同的


#浅拷贝  copy 创建了一个新的对象
lis3 = ["金毛狮王", "白眉鹰王", "紫衫龙王", "青衣福王"]
lis4 = lis3.copy()
#此时地址
print(id(lis3))
print(id(lis4))
#发现地址已经不一样了 ，证明不是对同一个地址进行操作
lis3.append("菜狗")
print(lis3)
print(lis4)
#此时两个列表不再具有相同操作   


#深拷贝
import copy
lis5 = ["金毛狮王", "白眉鹰王", "紫衫龙王", "青衣福王",['1','2']]
lis6 = copy.deepcopy(lis5)
lis5[4].append("3")
print(lis5,lis6)



###为什么有深浅拷贝？？###
###因为拷贝比创建新的对象容易的多###
