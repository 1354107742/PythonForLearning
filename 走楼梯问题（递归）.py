#走楼梯问题的动态求解（暴力递归）
def get_count(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	else:
		return get_count(n - 1) + get_count( n - 2)
print(get_count(10))