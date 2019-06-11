#ex1
#1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
#ans：True

#ex2
#利用while实习猜数字大小游戏
#num = 66
#while True:
#	a = int(input("输入你猜测的数字")) 
#	if num > a:
#		print("你的数字猜小了")
#		continue
#	elif num < a :
#		print("你的数字猜大了")
#		continue
#	else:
#		print("congratulation")
#		break


#ex3
#用循环输出1 2 3 4 5 6  8 9 10
#n = 0
#while n < 10 :
#	n = n + 1#应该设置在条件避开七的上面，否则会陷入无限循环
#	if n == 7:#避开
#		continue	
#	print(n)
	

#ex4
#输出100以内（不包括100）奇数和-偶数和的结果
#sum = 0
#n = 1 
#while n < 100:
#	if n % 2 == 1:
#		sum += n
#		pass
#	else :
#		sum -= n
#	n += 1
#print(n)


