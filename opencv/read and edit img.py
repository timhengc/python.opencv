import cv2
import numpy as np
import stackImg

img = cv2.imread("C:/Users/28151/Desktop/python/practice/opencv/CLK.jpg")  # (创建对象img)读取图片，通道顺序（B,G,R）

kernel =  np.ones((5,5),np.uint8) #创建矩阵

print(img.shape)#高度，宽度，chanel（3=BGR）

img = cv2.resize(img,(400,300)) #调整大小（宽度，高度），非矢量变化
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰色图 cvtColor = conver to color
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)  #模糊
imgCanny = cv2.Canny(img,150,200)   #勾勒
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) #膨胀（加粗勾勒线条）iterations=粗度
imgEroded = cv2.erode(imgDilation,kernel,iterations=1) #收缩/削弱
imgCropped = img[0:150,200:400]  #剪裁，高度，宽度 (左上角为0点)
imgHor = np.hstack((img,img))#水平拼接（必须大小，色调模式一致，也就是img.shape一致）
imgVer = np.vstack((img,img))#垂直拼接（必须大小，色调模式一致，也就是img.shape一致）
imgStack = stackImg.stackImages(0.5,([img,imgGray,img],[img,img,img])) #用stackImg中的函数自由拼接，不受限。（大小，（[第一行],[第二行]））
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#转换成色彩模型，HSV=Hue色度, Saturation饱和度, Value



cv2.imshow("CLK", img) #展示图片
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Eroded", imgEroded)
cv2.imshow("Cropped", imgCropped)
cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.imshow("Multiple Stack",imgStack)
cv2.imshow("HSV",imgHSV)


cv2.waitKey(0) #延时n ms（0=无限）


