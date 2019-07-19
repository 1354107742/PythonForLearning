#列表删除
list = ["Python","C++","Java",'Go','Javese','JavaSE']

#第一种clear()函数
#list.clear()
#print(list)

#第二种for循环变量
#这种删除的时候直接删是无法实现的，因为会改变索引结构
#del_list = []
#for el in list:
#    del_list.append(el)
#for el in del_list:
#    list.remove(el)
#print(list)

#删除java类语言
#lst = []
#for el in list:
#    for s in el:
#        if s == 'J':
#            lst.append(el)
#        continue
#for el in lst:
#    list.remove(el)
#print(list)

#字典的一点相关问题
#dic = {"a":"123"}
#s = dic.fromkeys("德玛西亚","盖伦")
#
# print(s)
#print(dic)
#s是创建一个新的字典，跟前面的dic字典是没有任何关系的
#这是一个很关键的问题