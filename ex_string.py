#ex1
#字符串的首字母大小写转换
s = "I'm so cool ,no expect"
s1 = s.capitalize()#首字母大写,必须要还给新字符串
print(s)#s不改变
print(s1)#s的首字母变成大写

#ex2
#字符串全大写或者小写
s = "I'm so cute, no reason"
ss = s.lower()#转换为小写
sss =  s.upper()#转换为大写
print(s)#不改变
print(ss)#s变为小写
print(sss)#s变为大写
#用于不区分大小写的程序上

#ex3
#字符串中的大小写互相转换
s = "Haha you Are my Empty"
print(s.swapcase())#将s中的大写变小写  小写变大写

#ex4
#这是将特殊符号后的第一个字母转换为大写
s = "Thanks, you for *watching my ex"
print(s.title())#you变为You  watching变为Watching

#ex5
#将字符串集中到你的符号上
s = "flower in my ground"
print (s.center(100,"*")

#ex6
#去空格
username = input("用户名:").strip()
password = input("密码：").strip()
if username = "hello" and password = "world":
	print("登陆成功")
else:
	print("登录失败")
#可以防止误输入空格


	
#ex7
#strip的删除
s = “asdfghjkla"
print(s.strip("a"))
#只会删除左右两边含有该字符的
 
#ex8
#字符串的替换
s = "Lixiaoming  is  a  pretty good boy"
ss = s.replace("Lixiaoming","xiaoxue") 
print(ss)
#输出为xiaoxue is a pretty good boy

#ex9
#字符串切片
s = "THX,I,love,you"
list = s.split(",") #利用“,”来切开这个字符串
print(list)#输出形式是列表

