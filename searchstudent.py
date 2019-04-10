#接收统计的学生样例
for i in range (int(input())):
#学生号
	m =int(input())
	massage = []
	for j in range(m):
		sp = list(input().split(" "))
		massage.append(sp)
#要查询的信息
	o = input()
#遍历列表
	for i in range(m):
		if (massage[i][0] == o):
			print(' '.join(map(str,massage[i])))