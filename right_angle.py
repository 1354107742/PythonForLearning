#计算是否为直角三角形
import math

#接受样例
n = int(input())
#输入三个点的相关参数
for i in range(n):
	x1,y1,x2,y2,x3,y3 = map(int,input().split())
	#用根函数和幂函数将边具象化
	sidefir = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
	sidesco = math.sqrt(pow(x1 - x3,2) + pow(y1 - y3,2))
	sidethi = math.sqrt(pow(x2 - x3,2) + pow(y2 - y3,2))
	#利用勾股定理进行验证
	if(pow(sidefir,2) == pow(sidesco,2) + pow(sidethi,2)):
		print("yes")
	elif(pow(sidesco,2) == pow(sidefir,2) + pow(sidethi,2)):
		print("yes")
	elif(pow(sidethi,2) == pow(sidefir,2) + pow(sidesco,2)):
		print("yes")
	else:
		print("no")
#输出相应的周长
print( sidefir + sidesco + sidethi)