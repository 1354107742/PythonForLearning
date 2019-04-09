from math import sin,radians
#获取样例数量
n = int(input())
#对两个边进行输入
for i in range(n):
	
	a,b = map(int,input().split())
	#正弦比较
	r = sin(radians(a-b))
	print('{:.2f}'.format(r))