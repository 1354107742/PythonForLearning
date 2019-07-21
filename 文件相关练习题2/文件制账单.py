f = open("文件相关练习题2\账单.txt",mode = "r" ,encoding = "utf-8")
s = f.readline()
ss = s.split()
print(s)
rea = []
for li in f:
    dic = {}
    ll = li.split()
    for i in range(len(ll)) :
        dic[ss[i]] = ll[i]
    rea.append(dic)     
print(rea)
