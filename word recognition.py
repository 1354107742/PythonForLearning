#输入一个英文句子，把句子中的单词(不区分大小写)按出现次数按从多到少把单词和次数在屏幕上输出来
#要求能识别英文句号和逗号，即是说单词由空格、句号和逗号隔开。
try:
    while True:
	#创建字典
        dict_sent = {}
        string = input()
		#将逗号和句号替换成空格
        string = string.replace(',',' ').replace('.',' ')
        #小写化处理
		string = string.lower()
		#切片
        string = string.split()
		#排序
        string.sort()
		#计数
        for item in string:
            dict_sent[item] = dict_sent.get(item, 0) + 1
        dict_sent = sorted(dict_sent.items())
		#字典输出
        for i in dict_sent:
            print('%s:%s' % i)
except:
    pass
