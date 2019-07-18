i = 1
while i < 11:
    grade  = int(input("请第%d位评委打分：" %i))
    if grade > 10 or grade < 5 :
        continue
    else:
        print(grade)
    i += 1