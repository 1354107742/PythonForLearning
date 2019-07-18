###encode###

#s = "alex"
#print(s.encode('utf-8'))#编码
#输出的B为bytes的形式

#s = "饿了吗"
#print(s.encode('utf-8'))
#一个算一个字节，UTF中一个字要用三个字节来表示
#print(s.encode('gbk'))
#在gbk中一个字要用三个字节来表示

###decode###
#s = "饿了吗"
#s1 = s.encode('utf-8')
#print(s1.decode('utf-8'))
#print(s1.decode('gbk'))
#编码和解码类似于一个密钥和密码本，如果编码和解码不对应那么得到的结果也不对 
#所以：
#     用什么编码 就用什么解码

