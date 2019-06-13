#ex1:
#基本形式
# dic = {"dic":"周杰伦","jj":"林俊杰","eason"："陈奕迅"}
# print(dic)

#ex2:
#Ture 和 False在字典中具有key功能
# dic = {1:"马化腾",False:"阿里巴巴",True:"马云"}
# ture和1 在字典中仍然等价
# print(dic)

#ex3:
#列表不可hash  而元祖可以
# dic = {1:"马化腾",False:"阿里巴巴",True:"马云",(1,"haha"):"元祖"}
# dic1 = {1:"马化腾",False:"阿里巴巴",True:"马云",[1,"haha"]:"列表"}
# print(dic)
# print(dic1)


#ex4:
#索引添加（这种会替换）
# dic = {'Mrs.kun':'周杰伦的老婆'}
# dic['国际章'] = '汪峰的老婆'
# print(dic)
# dic['国际章'] = '汪峰的老小婆'
# print(dic)
# setdefaul添加(这种不会替换)
# dic.setdefault("马蓉","王宝强")
# print(dic)
# dic.setdefault("马蓉","宋哲")
# print(dic)


#ex5:
#删除操作
# dic = {'Mrs.kun':'周杰伦的老婆','dic':'周杰伦','jj':'林俊杰','eason'：'奕迅'}
# pop删除
# ret = dic.pop("Mrs.kun")
# del删除
# del dic("Mrs.kun")
# clear删除
# dic.clear()
# popitem()随机删除操作
# ret = dic.popitem()

#ex6:
dic = {"name":"宋江","小李广":"华融","黑旋风":"李逵"}
dic["大宝剑"] = "盖伦"
print(dic["黑旋风"])
print(dic.get("黑旋风"))