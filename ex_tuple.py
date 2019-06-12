ex1：
#列表类型是list
lst = (1,"花生","芝麻")
print(type(lst))


ex2：
#元祖只有一个的时候 ，是该元素的类型，不过可以用逗号避免
tu = ("字符串")
print(type(tu))
#输出的是字符串类型
tu2 = ("字符串",)
print(type(tu2))
#输出的是元祖类型

ex3：
tu = ("DNF","CF","LOL","HC")
print(tu[2:])
#元祖切片操作和列表是一样的


ex4：
tu = ("DNF","CF","LOL","HC")
for el in tu:
	print(el)
#遍历仍然和列表一样


ex5：##错误反例
tu = ("DNF","CF","LOL","HC")
tu[2]  = "王者荣耀"
#这样的操作对于元祖来说会报错


ex6：
tu = (1,"马化腾",["胡辣汤","胡辣汤","粘玉米"],"帅气的我"）
tu[2].append("绿豆冰沙")
print(tu)
#此时tu输出的内容中有 “绿豆冰沙”！
#然而！元祖本身是没有动的，动的知识内存中的列表信息

ex7:
tu = ("DNF","CF",("the shy","JKL","baolan" ),"LOL","HC")
print(tu[2][3])
#元祖的嵌套结构跟列表一样

