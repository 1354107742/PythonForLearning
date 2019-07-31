#找出lis表中小于两个字符的 ，并且大写输出
lis = ["lalala","haha","aa","boomshakalaka","ba"]
lis1  = [i.upper() for i in lis if len(i) <= 2]
print(lis1)

#求元祖列表中（x,y）的循环方法 x取偶数，y取奇数
lst = [(x,y) for x in range(5) if x % 2 == 0 for y in range(5)  if y % 2 == 1]
print(lst)

#从lis2中 将3，6，9组合成新的列表
lis2 = [[1,2,3],[4,5,6],[7,8,9]]
print([i[2] for i in lis2])

#求出50以内能被3整除的数的平方
lis3 = [a**2  for a in range(50) if a % 3 == 0]
print(lis3)

#输出20以内所有偶数
print([x for x in range(0,20,2)])

#追加列表所属位置
lis4 = ["德玛西亚","爱吃","鸡蛋面"]
print([lis4[i] + str(i)  for i in range(len(lis4))] )

#提取里面的元素，变成新的列表
x = {
    'name': 'alex',
    'Values': [{'timestamp': 1517991992.94, 'values': 100, },
               {'timestamp': 1517992000.94, 'values': 200, },
               {'timestamp': 1517992014.94, 'values': 300, },
               {'timestamp': 1517992744.94, 'values': 350},
               {'timestamp': 1517992800.94, 'values': 280}
               ], }

lis5 = [[i["timestamp"],i["values"]] for i in x['Values']]
print(lis5)