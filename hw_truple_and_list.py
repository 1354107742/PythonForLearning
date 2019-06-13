#hw1:
#反转
# li = ["hi" ,"hello","world"]
# li.reverse()
# print(li)

#hw2:
#迭代添加字符串
# li = ["hi" ,"hello","world"]
# s = "qwertyu"
# li.extend(s)
# print(li)

#hw3:
#切片操作
# li = [1,2,3,4,5,6,"a",7,"b"]
# li2 = li[:3]
# print(li2)
# li3 = li[::-1]
# print(li3)

#hw4:
#迭代列表
# lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],"ab","data"]]
# print(lis)
# lis[3][2][1][2] = lis[3][2][1][2].replace("1","101")
# print(lis)


#hw5:
#替换逗号
# lis = ["alex","daka","thefy"]
# s = ""
# for el in lis:
	# s  += el + "_"
# print(s[:-1]) 

#hw6：
#索引数字
# lis = ["alex","daka","thefy"]
# count = 0
# for el in lis:
	# print(count)
	# count += 1
	
#hw7:
#range100以内偶数，并且放入列表
# list = []
# for el in range(0,101,2):
	# list.append(el)
# print(list)

#hw8:
#r查找出能被3整除的数，并将其放入列表
# list = []
# for el in range(0,51):
	# if el % 3 == 0 :
		# list.append(el)
# print(list)

#hw9
#倒序打印
# for el in range(100,0,-1):
	# print(el)

#hw10:
#range1~30,放入列表，并查找列表中被3整除的数
# lst = []
# new_lst =[]
# for el in range(0,31):
	# lst.append(el)
# print(lst)


# for el2 in lst:
	# if el2 % 3 == 0:
		# el2 = "*"
	# new_lst.append(el2)
# print(new_lst)

#hw11:
#查找以a并且以c结尾的所有元素
# li = ["taibai","alex","Adafjwic","adfcdfcc","fda"]
# lst = []
# for el in li:
	# if (el.startswith("a") or el.startswith("A") and el.endswith("B")):
		# print(el)