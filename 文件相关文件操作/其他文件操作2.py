import os #系统级模块
with open("文件相关文件操作\这是第六个测试文档.txt", mode="r", encoding="utf-8") as f1, open("文件相关文件操作\这是第七个测试文档.txt", mode="w", encoding="utf-8") as f2:
    s = f1.read()
    ss = s.replace("我","你")
    f2.write(ss)
os.remove("文件相关文件操作\这是第六个测试文档.txt")



