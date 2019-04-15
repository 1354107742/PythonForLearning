#实现：将M进制的数X转换为N进制的数输出。
#获取转换前进制和转换后的进制
M,N = map(int,input().split())
#获取需要转换的数字（顺便表明进制）
X = int(input(),M)
#利用字符串转换完的数进行排序
def conversion(X,N):
	a = ""
	while X > 0:
		#调用了divmod函数来返回商和余数
		X,i = divmod(X , N)
		a = num[i] + a
	return a
#从字符串中查找到相应数
num = "0123456789abcdefghijklmnopqrstuvwxyz"

print(conversion(X,N))
