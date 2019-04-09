#输入用例数 
#用例格式 
#input ： 1
#          1990 08 27

import datetime
for i in range(int(input())):
	print(datetime.datetime(*map(int,input().split())).strftime("%j").lstrip("0"))