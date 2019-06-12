#ex1
#list = ["王超","佳航","鹏飞","佳伟"]
#print(list)
#索引修改
#list[0] = "万毅"
#print(list)
#切片修改
#list[1:3] = ["王群"]
#print(list)#从结果可以看出这是个迭代修改方式
#查询
#for el in list :#element
#	print(el)

#ex2
#列表的增删改查练习
#lst = ["赵日天","洛天依","初音未来","一米六的兵长"]	
#查询长度
#print(len(lst))
#计数
#print(lst.count("初音未来"))


#ex3
#排序
# lst =[1,5,6,7,87,23,123,6,98,367,69,92]
# lst.sort()#快排
# print(lst)
# lst.sort(reverse = True)#倒序
# print(lst)

#ex4
#列表的嵌套
lst = [ 1,"the wu ","the sun",["hi,boy",["hey ,guy"],"hello,world"]
print(lst[3][1][0])
#嵌套添加
print(lst[3][1].append("芬达"))
