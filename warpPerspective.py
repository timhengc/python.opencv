import cv2
import numpy as np

img = cv2.imread("C:/Users/28151/Desktop/python/practice/opencv/CLK.jpg")  # 读取图片

width,height = 600,300

img = cv2.resize(img,(1000,600)) #调整大小（宽度，高度），非矢量变化

pts1 = np.float32([[300,300],[600,300],[300,800],[600,800]])#取原图4个点
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])#d定义输出图4个点
matrix = cv2.getPerspectiveTransform(pts1,pts2)#转换
imgOutput = cv2.warpPerspective(img,matrix,(width,height))#扭转视角(翘曲透视，将斜躺的部分掰正)

cv2.imshow("image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)



