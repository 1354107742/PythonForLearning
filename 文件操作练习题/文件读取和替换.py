import os
with open("文件操作练习题\马化腾.txt", mode="r", encoding="utf-8") as f1, open("文件操作练习题\马化腾2.txt", mode="w", encoding="utf-8") as f2:
    s = f1.read()
    print(s)
    ss = s.replace("马化腾是一个热爱游戏抄袭", "身为大魔王的我又来捣乱啦\n马化腾是一个热爱游戏抄袭")
    f2.write(ss)
    f1.close()
    f2.close()
os.remove("文件操作练习题\马化腾.txt")
os.rename("文件操作练习题\马化腾2.txt","文件操作练习题\马化腾.txt")


    

