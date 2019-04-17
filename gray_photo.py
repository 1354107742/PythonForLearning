#将图片装换为字符画的一个小程序
import matplotlib.pyplot as plt 
#设置在CMD中显示的大小
show_heigth = 30
show_width = 40

#随便打点字母来创建一个ascii字符列表
ascii_char = list("12uauf20u390rjslkj8!@#$%^&*()(*&^%#@$%^&*(")
char_len = len(ascii_char)

#利用plt.imread方法将图片读取出来，对于彩图，返回size = heigth * width *3的大小
#matplotlib中色彩排列遵循RGB顺序
#opencv包中的cv2排列是BGR顺序
pic = plt.imread("图片名以及其绝对路径")

#现在开始获取图片的高和宽
pic_heigth,pic_width,_ = pic.shape

#最重要的就是灰度图的制作，以下代码是实现灰度图转换的
#对于灰度图的制作我其实也是不怎么了解的，这个代码是在网上百度到的
#大致原理是将RGB进行相应的权值改变使颜色发生根本的改变
gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]

#这样就可以利用当前灰度图产生的各个像素的灰度值，将其映射到asscii列表上
for i in range (show_heigth):
    #根据自己在前面设置的像素产生对应灰度图
    y = int(i * pic_heigth / show_heigth)
    text = ""
    for j in range (show_width):
        x = int (j * pic_width / show_width)
        text += ascii_char[int(gray[y][x] / 256 * char_len)]
    #现在就有一个属于你的字符画啦
    print(text)