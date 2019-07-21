f = open("文件操作练习题\马化腾.txt",mode = "r+" ,encoding = "utf-8")
s = f.read()
print(s)
f.write("啦啦啦啦，德玛西亚")
f.flush()
print(s)
f.close()

