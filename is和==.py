#== 比较  比较的是值
#a = 'alex'
#b = 'alex'
#print(a == b)
#li1 = [1,2,3]
#li2 = [1,2,3]
#print(li1 == li2)

#is 是比较 比较的是内存地址
#a = 'alex'
#print(id(a))
#对于列表，字符串，数值都有自我的内存地址

a = 'alex'
b = 'alex'
print (a is b)  #true
n = 10
m = 10
print (n is m)   #true
#对于小数据池-5~256都为true  n = 1000
#字符串中如果有特殊字符他们的内存地址就不一样例如  a ='alex@'
li = [1,2,3]
li2 = [1,2,3]
print (li is li2) #false
tu = (1,2,3)
tu1 = (1,2,3)
print (tu is tu1) #false
dic = {'name':'alex'}
dic1 = {'name':'alex'}
print (dic is dic1)#false

#总结：
            #== 比较值 比较的是两边的值
            #is 比较地址 比较的是两边对象的内存 
            
