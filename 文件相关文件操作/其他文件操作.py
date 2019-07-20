f1 = open("文件相关文件操作\这是第五个测试文档.txt", mode="r+", encoding="utf-8")
#光标在读取后，是不会回复到原来位置的
s = f1.read(3)
print(f1.tell())#tll()是告知光标位置函数
ss = f1.read(3)
print(f1.tell())
print(s)
print(ss)
f1.seek(0)
###不管读了几个，如果执行W操作，都是从后面写，不是从光标后面写###
###如果没有没有移动光标，那么就是在开头进行覆盖###
print(f1.tell())
print(s)
#seek(0,2)有三个参数  0 表示开头   1 表示当前位置  2 表示结尾





