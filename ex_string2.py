#ex1
#之前的格式化输出
s12 = "my name is %s ,im %d years old,i like %s" %("haha",18,"hehe")
#可以用{}来代替
s13 = "my name is {} ,im {} years old,i like {}" .format("haha",18,"hehe")
#format的格式化输出可以用编号来引入
s14 = "my name is {0},im {1} years old,i like {}" .format("haha",18,"hehe")
#format也可以用名字来引入
s15 = "my name is {name},im {age} years old,i like{mingxing}" .format(name = "hehe",age = "18 ",mingxing = "hehe")

#ex2
#判断查找和删除
s = " 聪明人的月饼是粽子 "
print(s.startswith("月饼"))#判断是否以月饼开头  结果false
print(s.startswith("聪明人"))#判断是否以聪明人开头 结果True
print(s.endswith("月饼")#判断是否以月饼结尾 结果false
print(s.endswith("粽子")#判断是否以粽子结尾 结果True、

print(s.find("月饼") #计算在字符串中月饼的位置（根据查找字数来计数）
					#也就是说，这个的位置是3
print(s.find("月饼",3）#可以切片查找


#ex3
s = "123.16"
ret = len(s)#计算字符串的长度
print(ret) 

#ex4
count = 0 
s = "我实在是太tm帅了！！！"
while count < len(s):
	print(s[count])
	count = count + 1
#字符串循环输出
#等价于
s = "我实在是太tm帅了！！！"
for i in s：
	print(i)
	
