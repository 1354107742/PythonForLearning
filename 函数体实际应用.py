#求前n项和
def sum(n):
    s = 0
    count = 1
    while count <= n:
        s = s + count
        count += 1
    return s

#求N是奇数还是偶数
def fn(n):
    if n % 2 == 1:
        print("是奇数")
    else:
        print("是偶数")

ins = int(input("请输入你想要计算的值："))
s2 = sum(ins)
print(s2)
fn(ins)

