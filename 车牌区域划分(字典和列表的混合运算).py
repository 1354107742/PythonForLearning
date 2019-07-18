cars = ['鲁32184124', '鲁dfaflajl', '沪12341', '黑12314', '黑5466' ]
locals ={'鲁':'山东','黑':'黑龙江','沪':'上海'}
loca = {}
l = 0
for k,m in locals.items():
    for i in cars:
        for g in i:
            if g == k:
                l += 1
                loca[m] = locals[k]
                loca[m] = l
    l = 0
print(loca)
