#建立一个求一元二次方程解的类（a*x2+b*x+c=0），输入系数a,b,c 的值后打印出这个方程的解。

import math
 
def Solution(a, b, c):
    if a == 0:
        if b == 0:
            return '-1'
        return 'x=%.2f'%(-c/b)
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b - math.sqrt(delta))/(2*a)
            x2 = (-b + math.sqrt(delta))/(2*a)
            return 'x1=%.2f,x2=%.2f'%(x1,x2)
        elif delta == 0:
            return 'x=%.2f'%(-b/(2*a))
        else:
            return '-1'
			
#样例输入
test = int(input())			
for i in range(test):
	list_abc = list(map(int,input().split()))
	print(Solution(list_abc[0],list_abc[1],list_abc[2]))