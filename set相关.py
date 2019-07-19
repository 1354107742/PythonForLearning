s = {"a","LOL","123"}
s1 = {"123", "123", "3242", "3242", "1234", "1234"}
print(s)
print(type(s))

###set不可插入字典和列表###
#s = {[1,2,3]}
#print(s)
#这是会报错的

#set核心功能 ，去重复
lit = ["123","123","3242","3242","1234","1234"]
#大量无用重复
print(lit)
# 利用set()去重
se = set(lit)
#此时se是一个set
print(se)
#我们需要转换回列表
lit = list(se)
#此时，lit变成为去重后的列表
print(lit)

#增加
s.add("马化腾")
print(s)
#删除(指定)
s.remove("马化腾")
print(s)
#删除(随机)
s.pop()
print(s)

#set是无法修改的，只能先删除再添加
#交集
print(s & s1)
#并集
#前面有个POP()所以会缺少一个元素
print(s | s1)
#差集
print(s1 - s)



#frozenset冻结set函数是可以hash的
set2 = frozenset([1,2,4,4,5,6])
print(set2)
set3 = {"a",set2}
print(set3)