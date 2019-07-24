s = "Welcome to Beijing"
for c in s:
    print(c)

# 可迭代对象: str, list, tuple, set, f, dict
# 所有的以上数据类型中都有一个函数__iter__(), 所有包含了__iter__()的数据类型都是可迭代的数据类型 Iterable
# dir()来查看一个对象,数据类型中包含了哪些东西
# lst = [1,2,3]   # list
# # print(dir(lst))
# s = "王尼玛"
# print("__iter__" in dir(s))
# print("__iter__" in dir(lst))
# print("__iter__" in dir(123))


lst = ["haha","hehe","wakaka"]
it = lst.__iter__()
print(it.__next__())

#Iterable和Iterator可以用来判断是否为可迭代对象 ，迭代器
#利用isinstance()函数
from collections import Iterable
from collections import Iterator
print(isinstance(lst,Iterable))
print(isinstance(lst,Iterator))