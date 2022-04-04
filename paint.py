import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #生成黑色图片，zero代表黑色，512x512的矩阵

#print(img)#打印矩阵
print(img.shape) #打印参数list，【0】=宽高，【1】=宽度

img[:]= 255,255,255 # ：代表完整的图片size [0:100,200:300]可以指定size; B,G,R

cv2.line(img,(100,200),(300,400),(255,0,120),10) #画线（图，起点x,y，终点，颜色，粗细）
cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(0,225,0),10)#画空心矩形
cv2.rectangle(img,(230,230),(260,260),(0,0,225),cv2.FILLED)#画实心矩形
cv2.circle(img,(250,250),50,(90,250,225),10)#画圆（圆心，半径，颜色，粗细）
cv2.putText(img,"ABC",(200,100),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,0),3)#写字（文本，起点，格式用cv2.FONT搜,字号，颜色，粗细）


cv2.imshow("image",img)
cv2.waitKey(0)
