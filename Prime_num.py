#质因数分解问题
n = int(input())
res = 0
#
while n >1:
    flag = 1
    #方根是为了检验当前的N是否还有质因数
    t = int(n**0.5)
    #同时用N的方根T+1遍历 也极大缩小了遍历时间
    for i in range(2,t+1):
        #如果查到以后 FLAG置0 结束当前循环
        if n % i == 0:
            n /= i
            res += 1
            flag = 0
            break
    #如果FLAG为1 则表示当前已经没有素数可以满足条件了
    if flag:
        #剩下的余数必定是一个质因数 所以要加一
        res += 1
        break
print(res)