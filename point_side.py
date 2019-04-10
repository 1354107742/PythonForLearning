import math
#获取测试用例
n = int(input())
#获取两点间的坐标
for i in range (n):
	x1,y1,x2,y2 = map(int,input().split())
	side = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
print("%.2f"%side)