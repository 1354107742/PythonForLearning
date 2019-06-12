#字符串处理练习

# name = "aleX leNb"
 hw1：输出e所在的输出位置
# s =  name.find("e",0,5)
# print(s)
# s2 =  name.find("e",5)
# print(s2)
hw1_2:利用循环完成
# count = 0
# while count < len(name):
	# if name[count] == "e":
		# print(count)
	# count = count + 1

	
# name = "aleX leNb"	
hw2：将A变成大写，然后输出结果
# s1 = name[:1]
# s2 = name[1:]
# print(s1.upper() + s2)
hw2_1:利用replace
# name.replace("a","A")


hw3:将s切片成为新的字符串s1 = ”123“
# s = "123a4b6c"
# s1 = s.split[0:3]

#s = "asdfer"
hw4:对字符串进行for循环每次打印的都是他自身
#for c in s:
#	print(s)



# s = "asdfer"
 hw5:每次循环后加上一个sb
# d = "sb"
# for c in s:
	# print(s + d) 

	
# s = "321"
hw6:对s进行循环，依次输出为倒计时3,倒计时2，倒计时1
# for c in s:
	# print("倒计时 {} 秒",.format(s[c]))
# else:
	# print("出发！")


	
 hw7:实现一个加法计数器
# content = input("请输入计算的公式:")
# res = content.split("+")
# s1 = res[0]
# s2 = res[1]
# a = int(s1)
# b = int(s2) 
# print(a+b)


hw8:查看字符串中有几个数字 如：ttd67tsa67t126787f
# content = input("请输入内容：")
# count = 0 
# for c in content:
	# if c.isdigit():
		# count  = count+1
# print(count) 

hw9:导航模拟

# while True:
	# choose = input("请做出你的选择：\t").strip().upper()
	# if choose == "A":
		# print("走大路回家")
		# choose2 = input("请选择回家方式（公交车还是步行）：").strip()
		# if choose2 == "公交车":
			# print("this is will spend 10 mins ")
			# break
		# elif choose2 == "自行车":
			# print("this is will spend 20 mins ")
			# break
		# else:
			# continue
	# elif choose == "B":
		# print("你选择了从小路回家")
		# break
	# elif choose == "C":
		# print("你选择绕道回家,请选择游戏:\n游戏厅还是网吧")
		# choose3 = input("请做出你的选择:\t")
		# if choose3 == "游戏厅":
			# print("you will spend 1hour30mins and your parents will wait you with angry")
			# continue
		# elif choose3 == "网吧":
			# print("you will spend 2hours and your parents will hit your ass!")
			# continue


hw10：100以内奇数相加  偶数相减  不包括88
# count = 1
# sum = 0
# while count < 100:
	# if count % 2 == 0:
		# sum -= count
	# elif count == 88:
		# count ++
	# else:
		# sum += count

		
hw11： 判断回文字
# s = "上海自来水来自海上"
# s1 = s[::-1]
# if s == s1:
	# print("是回文")
# else:
	# print("不是回文")
	
hw12 :输入一个字符串 看大写，小写，其他字符分别有多少个
# content = input("请输入一个字符串")
# num_count = 0	
# upper_count = 0
# lower_count = 0
# for c in content:
	# if c.isdigit():
		# num_count += 1
	# elif c.isupper():
		# upper_count += 1
	# elif c.islower():
		# lower_count += 1
# print("你本段字符串的大写字母有{}个，小写字母有{}个，数字有{}个。" .format(upper_count,lower_count,num_count))
