youtuber = {' 杨树':25500,'寅子':32613,'女流':3124412,'王老菊':2131231 }
sum = 0
#计算主播平均收益
for value in youtuber.values():
    sum += value 
aver = sum / len(youtuber)
print(aver)

#计算当前收益小于平均值的主播
lst =[]#标记要删除的元素
for youtuber1,val in youtuber.items():
    if val < aver:#判断条件
        lst.append(youtuber1)#无法直接迭代删除字典所以将所需key加入到列表
for el in lst:
    youtuber.pop(el)#从列表中删除字典中的key
print(youtuber)

#手动删除掉王老菊
youtuber.pop('王老菊')
print(youtuber)

