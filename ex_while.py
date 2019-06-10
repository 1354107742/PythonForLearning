#解决print输出方案的解决方法


#ex1：
#在无明确需求的情况下要避免无限循环
while True：
	print("hey,mother fucker")

#ex2：
count = 1
while count <= 10:
		print("hello,mother fucker")
		count + 1
   
#ex3:
while True:
	s = input("input you say to others:")
	if s == 'q'
		break
	print (s)#在判定下方，保证如果输入Q时不会打印Q、

#ex4:
while True:
	s = input("input you say to others:")
	if s == 'q'
		break
	#添加屏蔽字
	if "mother fucker" in s:#对比字符串中的数字，无法区分内容的
		print("your word can not to input in window")
		continue#回到上一层循环
	print (s)#在判定下方，保证如果输入Q时不会打印Q
	
#ex5：
#100以内奇数的算法
count = 1
sum = 0 
while count <= 100:
	print(count)
	if count % 2 == 1:
		sum = sum + count
print(sum)

#ex6:用更优化的方式输出注释内容
#print("alex是一个老头，爱好女，性别男 )
#print("hony是一个老头，爱好男，性别男)
#print("john是一个老头，爱好不详，性别男)
#print("hex是一个老头，爱好XX，性别男 )
name = input("请输入名字：")
hobby = input ("请输入你的爱好:")
gender = input("请输入你的性别:")
#pirnt(name + "是一个老头,爱好是"+ hobby + ",性别," + gender ) 
pirnt("%s是一个老头,爱好是%s,性别%s" %(name ,hobby,gender) ) 
