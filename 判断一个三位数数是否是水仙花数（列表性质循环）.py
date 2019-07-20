n = input("请输入你想要判断的数字：")
s = int(n[0])**3 + int(n[1])**3 + int(n[2])**3
if int(n) == s:
    print("是水仙花数")
else:
    print("不是水仙花数")