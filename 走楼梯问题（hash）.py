#走楼梯问题的备忘录算法（hash表法）
def get_count(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		l = [1,2]
		#因为每个递归只跟前两个数有关，所以只取前两个
		for i in range(3,n):
			l[0],l[1] = l[1],l[0]+l[1]
		return l[0] + l[1]
print(get_count(10))