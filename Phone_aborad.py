#按照手机键盘输入字母的方式，计算所花费的时间 
#如：a,b,c都在“1”键上，输入a只需要按一次，输入c需要连续按三次。
#如果连续两个字符不在同一个按键上，则可直接按，如：ad需要按两下，kz需要按6下 
#如果连续两字符在同一个按键上，则两个按键之间需要等一段时间，如ac，在按了a之后，需要等一会儿才能按c。 
#现在假设每按一次需要花费一个时间段，等待时间需要花费两个时间段。 
#现在给出一串字符，需要计算出它所需要花费的时间。

#构建一个按键的列表
while 1:
	try:
		get_str = input()
		#模拟键盘按键 将其放入列表中
		search_char = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		sum = 0
		index = -1
		for i in get_str:
			for j in range(len(search_char)):
				if i in search_char[j]:
					if index == j:
						sum += 2
					sum += search_char[j].index(i) + 1
					index = j
					break
		print(sum)
	except:
		break