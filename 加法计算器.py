dic = {"计算结果为：":None}
content  = input('请输入你想要计算的公式:').strip()
lis = content.split("+")
sum = 0 
for el in lis:
    sum += int(el.strip())
dic["计算结果为："] = sum
print(dic)