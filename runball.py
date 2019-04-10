#获取测试用例
n = int(input())
for i in range (n):
#利用切片将高度和弹跳次数进行统计
	high,count = list(map(int,input().split()))
	#保存初始高度
	run = high
	#进行第一次以后的高度运算
	for j in range(count-1):
			high = high / 2
			run = run + high * 2
	print("%.2f"%run)
	