dic = {
    '-':'fu',
    '1':'yi',
    '2':'er',
    '3':'san',
    '4':'si',
    '5':'wu',
    '6':'liu',
    '7':'qi',
    '8':'ba',
    '9':'jiu',
    '.':'dian'
}
ip = input("请输入你想学的数字：")
for i in ip:
    print(dic[i],end = " ")