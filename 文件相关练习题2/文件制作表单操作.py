list1 = []
f  = open("文件相关练习题2\文件制作表单操作.txt",mode = "r",encoding = "utf-8")
s = f.readline()
ss = s .split()
print(s)

for li in f:
    dic = {}
    list2 = li.split()
    for i in range(len(ss)):
        dic[ss[i]] = list2[i]
    list1.append(dic)
print(list1)



    
