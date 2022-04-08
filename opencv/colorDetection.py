import cv2
import numpy as np
import stackImg

def empty(a):
    pass


cv2.namedWindow("TrackBars")  #创建窗口
cv2.resizeWindow("TrackBars",640,240)  #调整窗口大小
cv2.createTrackbar("Hue Min","TrackBars",100,179,empty)  #创建拖动条。实际色度H属于0-360度，映射到变量是0-179 （具体看HSE解释.word文档）
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)  #（“bar 名”，“窗口名”，默认位置，最大值，函数）
cv2.createTrackbar("Sat Min","TrackBars",15,255,empty)   #饱和度S= 0-255代表0-100%
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",130,255,empty)  #明度V= 0-255代表0-100%
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
while 1:
    img = cv2.imread("C:/Users/28151/Desktop/python/practice/opencv/colors.png")  # 读取图片，通道顺序（B,G,R）
    img = cv2.resize(img,(400,300))  #调整大小（宽度，高度），非矢量变化
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)    #转换成色彩模型，HSV=Hue色度, Saturation饱和度, Value明度

    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")  #获取拖动条的值（拖动条名，窗口名）
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    
    lower = np.array([h_min,s_min,v_min])  #创建最小值数组
    upper = np.array([h_max,s_max,v_max])  #最大值数组

    imgMask = cv2.inRange(imgHSV,lower,upper)  #生成指定HSV范围内的Mask图片, 所需部分将以白色显示（即1），不需要的以黑色显示（即0）
    imgResult = cv2.bitwise_and(img,img,mask=imgMask) #将原图和imgMask相与，识别出特定展示区域。（原图，新图基于谁，mask）
    imgStack = stackImg.stackImages(1,([img,imgHSV],[imgMask,imgResult]))#拼接

    print(h_min,h_max,s_min,s_max,v_min,v_max,end="\r")  #打印拖动条的值
    cv2.imshow("Stack",imgStack)
 
    
    
    cv2.waitKey(1) #延时n ms（0=无限）