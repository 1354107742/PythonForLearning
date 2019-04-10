import math
#获取测试用例
n = int(input())
#获取球心和球心上的一点
for i in range (n):
	x1,y1,z1,x2,y2,z2 = map(int,input().split())
	#对半径进行公式求导
	parameter1 = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2) + pow(z1 - z2,2))
	#对体积进行求导
	V = 4 * pow(parameter1,3) / 3 * math.pi
print("%.2f %.2f"%(parameter1,V))