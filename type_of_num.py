#ex1:
#练习bit_length的整形练习
a = 3
print(a.bit_length())#3的二进制长度   

#ex2:
#字符串转换成数字（bool值的练习）
s = "128"
i = int(s)#将字符串抓换成数字
print(type(i))#现在的i是int

ss = str(i)
print(type(ss))#此时的ss是字符串
#综上所述，转换形式的使用方法
#所以bool值也可以
b = True
c = int(b)
print(c)#此时转换完bool值后，True为真，false为假


#ex3：
#int转换成bool
a = 100
b = bool(a)
print(b)
#此时的结论为，零为False  非零为True

#ex4：
s = ""
if s:
	print("哈哈")
else:
	print("呵呵")
#此时是false
s = "   "
if s:
	print("哈哈")
else:
	print("呵呵")
#此时为True


#ex5
#切片的实例用法演示
string = "123456789"
print(string[3])
#索引从零开始
print(string[-7])
#倒索引从一开始
print(string[3:6])
#只能取到第三个数字到第五个数字
print(string[0:2]+[3:6])
#切片具有可拼接性
print(string[2:])
#默认直接到结尾
print(string[:])
#默认从头开始
print(string[:])
#一个从头到尾的切片

#ex6
#切片语法：s[起始位置：结束位置：步长]
s  = "the world will better"
s1 = s[1:5:2]
#从[1:5]切片中 每有两个取一个


