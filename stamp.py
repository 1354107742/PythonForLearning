#邮票问题
a = 8#面值为八毛的有五张
b = 10#面值一块的有四张
c = 18#面值为一块八毛的有六张
s = []#组合数的值
#排列组合
for i in range(5):
	s1 = a * i
	s.append(s1)
	for j in range(4):
		s2 = a * i + b * j
		s.append(s2)
		for k in range(6):
			s3 = a * i + b * j + c * k
			s.append(s3)
#排序去重
s.sort()
news = []
for i in s:
	if i not in news:
		news.append(i)
#输出结果
for i in news:
	print(i)