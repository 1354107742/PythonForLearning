cars = ['鲁32184124', '鲁dfaflajl', '沪12341', '黑12314', '黑5466' ]
locafs ={'鲁':'山东','黑':'黑龙江','沪':'上海'}
l = 0
for k in locafs:
    for i in cars:
        for g in i:
            if g == k:
                l += 1
                locafs[k] = l
                print(locafs)
    l = 0
print(locafs)
