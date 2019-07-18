

 
lst = ['头号玩家','碟中谍','飞跃疯人院']
dic = {}
for i in lst:
    print("请给%s打一个你认为理想的分数" %i)
    grade  = int(input("您的分数是:"))
    dic[i] = grade
print(dic)