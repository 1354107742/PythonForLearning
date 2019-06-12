#ex1:
for i in range(10):#是打印10个数，不是打印到10
	print(i)

for i in range(3,7):#从3打印到7 ，但是不打印到7
	print(i)

for i in range(3,10,2):#从3到10，每两个取一个数
	print(i)

for i in range(10,1,-1):#倒序输出
	print(i)

#ex2：#之前问题的再扩展
sum = 0
for i in range(100):
	if i % 2 == 0：
		sum -= i
	else：
		sum += i