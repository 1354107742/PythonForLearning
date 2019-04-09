#对称平方数
for i in range(1, 256):
#如果遍历的字符串和倒序遍历的相同则输出
	if str(i * i) == str(i * i)[::-1]:
		print(i)