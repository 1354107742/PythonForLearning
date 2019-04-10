n = int(input())

for i in range (n):
	high,count = list(map(int,input().split()))
	run = high
	for j in range(count-1):
			high = high / 2
			run = run + high * 2
	print("%.2f"%run)
	