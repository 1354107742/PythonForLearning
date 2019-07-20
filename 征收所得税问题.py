money  = int(input('请输入你的个人所得：'))
income  = 0
if money < 2000:
    print("你的收入竟然都不用交税，真是可怜")
elif 4000 > money >= 2000:
    income = money - 2000 * 0.03
elif 6000 > money >= 4000:
    income = money - 2000 * 0.03 - 2000 * 0.04
elif 8000 > money >= 6000:
    income = money - 2000 * 0.03 - 2000 * 0.04 - 2000 * 0.08
else:
     income = money - (money - 10000) * 0.2
print(' 你的税后所得为：%d' %income)

