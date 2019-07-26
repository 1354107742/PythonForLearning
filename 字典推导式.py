dic = {"a":"b","c":"d"}
#将上面字典中的key与value互换
new_dic = {dic[key]:key for key in dic }
print(new_dic)

lst = [" 德玛西亚之力","德邦总管","死亡歌颂者"]
lst2 = ["盖伦","赵信","卡尔萨斯"]
dic = {lst[i]:lst2[i] for i in range(len(lst))}
print(dic)

