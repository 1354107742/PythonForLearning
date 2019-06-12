
while True:
	choose = input("请做出你的选择：\t").strip().upper()
	if choose == "A":
		print("走大路回家")
		choose2 = input("请选择回家方式（公交车还是步行）：").strip()
		if choose2 == "公交车":
			print("this is will spend 10 mins ")
			break
		elif choose2 == "自行车":
			print("this is will spend 20 mins ")
			break
		else:
			continue
	elif choose == "B":
		print("你选择了从小路回家")
		break
	elif choose == "C":
		print("你选择绕道回家,请选择游戏:\n游戏厅还是网吧")
		choose3 = input("请做出你的选择:\t")
		if choose3 == "游戏厅":
			print("you will spend 1hour30mins and your parents will wait you with angry")
			continue
		elif choose3 == "网吧":
			print("you will spend 2hours and your parents will hit your ass!")
			continue

