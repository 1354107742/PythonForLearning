#完数
result = []
for i in range(2,60):
	tmp = []
	for k in range(2,60):
		if k < i:
			if not i % k:
				tmp.append(k)
			else:
				continue
		else:
			break
	count = 0
	for m in tmp：
		count = count + m
	if count == i:
		result.append(i)
	else:
		continue
print ("result")