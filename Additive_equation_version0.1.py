#求1000以内满足 abc+bcc==532的所有abc的值
for a in range(1,9):
	for b in range(1,9):
		for c in range(1,9):
			if ((a * 100 + b * 10 + c + b * 100 + c *10 + c) ) == 532:
				print(a,b,c)
	