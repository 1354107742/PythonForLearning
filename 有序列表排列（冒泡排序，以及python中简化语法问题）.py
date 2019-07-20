#冒泡排序
lis = [1,45,76,15,75,3,8,94,52]
for a in range(len(lis)):
    i = 0
    while i < len(lis) - 1:
        if lis[i] > lis[i + 1] :
           lis[i],lis[i + 1] = lis[i + 1],lis[i]
        i += 1    
    print(lis)
