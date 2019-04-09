#反序相等
for i in range(1000,10000):
	if str(i) == str(i * 9)[::-1]:
		print(i)
	